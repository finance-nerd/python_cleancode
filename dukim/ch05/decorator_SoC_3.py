import time
from functools import wraps

import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def log_execution(function):
    @wraps(function)
    def wrapped(*args, **kwargs):
        logger.info("started execution of %s", function.__qualname__)
        ret = function(*kwargs, **kwargs)
        logger.info("ended execution of %s", function.__qualname__)
        return ret

    return wrapped


def measure_time(function):
    @wraps(function)
    def wrapped(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)

        logger.info(
            "function %s took %.2f",
            function.__qualname__,
            time.time() - start_time,
        )
        return result

    return wrapped



def operation():
    time.sleep(3)
    logger.info("running operation...")
    return 33

log_execution(measure_time(operation))()
logger.info("-------")
time.sleep(1)

measure_time(log_execution(operation))()