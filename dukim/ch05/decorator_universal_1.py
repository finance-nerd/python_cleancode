from functools import wraps

import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


class DBDriver:
    def __init__(self, dbstring):
        self.dbstring = dbstring

    def execute(self, query):
        return f"query {query} at {self.dbstring}"


def inject_db_driver(function):
    """This decorator converts the parameter by creating a ``DBDriver``
    instance from the database dsn string.
    """

    @wraps(function)
    def wrapped(dbstring):
        return function(DBDriver(dbstring))

    return wrapped


@inject_db_driver
def run_query(driver):
    return driver.execute("test_function")


class DataHandler:
    """The decorator will not work for methods as it is defined."""

    @inject_db_driver
    def run_query(self, driver):
        return driver.execute(self.__class__.__name__)

print(run_query("test ok"))

print(DataHandler().run_query("test fails"))