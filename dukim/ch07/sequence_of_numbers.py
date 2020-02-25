from dukim.ch07.log import logger

class SequenceOfNumbers:
    def __init__(self, start=0):
        self.current = start

    def __next__(self):
        current = self.current
        self.current += 1
        return current

    def __iter__(self):
        return self

if __name__ == "__main__":
    si = SequenceOfNumbers(100)
    logger.info(next(si))
    logger.info(next(si))
    logger.info(next(si))

    for t in zip(SequenceOfNumbers(), "abcdef"):
        logger.info(t)