from dukim.log import logger


class DBHandler:
    """Simulate reading from the database by pages."""

    def __init__(self, db):
        self.db = db
        self.is_closed = False

    def read_n_records(self, limit):
        return [(i, f"row {i}") for i in range(limit)]

    def close(self):
        logger.debug("closing connection to database %r", self.db)
        self.is_closed = True


def stream_db_records(db_handler):
    retrieved_data = None
    page_size = 10
    try:
        while True:
            page_size = (yield retrieved_data) or page_size
            retrieved_data = db_handler.read_n_records(page_size)
    except GeneratorExit:
        db_handler.close()


if __name__ == '__main__':
    streamer = stream_db_records(DBHandler("testdb"))
    next(streamer)
    logger.info(f'next default - {next(streamer)}')
    streamer.send(3)
    logger.info(f'next 3 - {next(streamer)}')
