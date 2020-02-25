from dukim.ch07.log import logger

class NumberSequence:
    def __init__(self, start=0, step=1):
        self.current = start
        self.step = step

    def next(self):
        value = self.current
        self.current += self.step
        return value


if __name__ == "__main__":
    si = NumberSequence(1, 2)
    logger.info(si.next())
    logger.info(si.next())
    logger.info(si.next())

    # zip(NumberSequence(), "abcdef")
