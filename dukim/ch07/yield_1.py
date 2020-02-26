from dukim.log import logger


def _chain(*iterables):
    for it in iterables:
        for value in it:
            yield value


def chain(*iterables):
    for it in iterables:
        yield from it


if __name__ == '__main__':
    logger.info(list(_chain("hello", ["world"], ("tuple", " of ", "values."))))
    logger.info(list(chain("hello", ["world"], ("tuple", " of ", "values."))))

