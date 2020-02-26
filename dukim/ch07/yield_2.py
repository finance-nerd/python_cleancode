from dukim.log import logger


def sequence(name, start, end):
    logger.info("%s started at %i", name, start)
    yield from range(start, end)
    logger.info("%s finished at %i", name, end)
    return end


def main():
    step1 = yield from sequence("first", 0, 5)
    step2 = yield from sequence("second", step1, 10)
    return step1 + step2


if __name__ == '__main__':
    g = main()
    logger.info(next(g))
    logger.info(next(g))
    logger.info(next(g))
    logger.info(next(g))
    logger.info(next(g))
    logger.info(next(g))
    logger.info(next(g))
    logger.info(next(g))
    logger.info(next(g))
    logger.info(next(g))
    logger.info(next(g))
