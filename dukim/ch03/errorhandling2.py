import logging, time

def connect_with_retry(connector, retry_n_times, retry_threshold=5):
    for _ in range(retry_n_times):
        try:
            return connector.connect()
        except ConnectionError as e:
            logging.info("%s: 새로운 연결 시도 %is", e, retry_threshold)
            time.sleep(retry_threshold)
    exc = ConnectionError(f"{retry_n_times} 번째 재시도 연결 실패")
    logging.exception(exc)
    raise exc

class DataTransport:
    retry_threshold: int = 5
    retry_n_times: int = 3

    def __init__(self, connector):
        self._connector = connector
        self.connection = None

    def deliver_event(self, event):
        self.connection = connect_with_retry(self._connector, self.retry_n_times, self.retry_threshold)
        self.send(event)

    def send(self, event):
        try:
            return self.connection.send(event.decode())
        except ValueError as e:
            logging.error("%r 잘못된 데이터 포함: %s", event, e)
            raise
