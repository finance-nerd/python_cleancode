from dukim.log import logger


class SequenceIterator:
    def __init__(self, start=0, step=1):
        self.current = start
        self.step = step

    # def __iter__(self):
    #     return self

    def __next__(self):
        value = self.current
        self.current += self.step
        return value


if __name__== '__main__':

    si = SequenceIterator(1, 2)
    logger.info(next(si))
    logger.info(next(si))
    logger.info(next(si))

    # for n in SequenceIterator():
    #     if n >= 10:
    #         break
    #     logger.info(n)