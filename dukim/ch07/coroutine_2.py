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


class CustomException(Exception):
    """An exception of the domain model."""


def stream_db_records(db_handler):
    while True:
        try:
            yield db_handler.read_n_records(10)
        except CustomException as e:
            logger.info("controlled error %r, continuing", e)
        except Exception as e:
            logger.info("unhandled error %r, stopping", e)
            db_handler.close()
            break


if __name__ == '__main__':
    streamer = stream_db_records(DBHandler("testdb"))
    logger.info(f'next {next(streamer)}')
    streamer.throw(CustomException)
    logger.info(f'CustomException {next(streamer)}')
    streamer.throw(RuntimeError)
    logger.info(f'RuntimeError {next(streamer)}')