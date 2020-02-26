import time

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
    try:
        while True:
            yield db_handler.read_n_records(10)
    except GeneratorExit:
        db_handler.close()


if __name__ == '__main__':
    streamer = stream_db_records(DBHandler("testdb"))
    logger.info(next(streamer))
    logger.info(next(streamer))
    streamer.close()