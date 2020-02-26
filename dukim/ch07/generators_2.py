from dukim.ch07._generate_data import PURCHASES_FILE, create_purchases_file
from dukim.ch07.log import logger
from itertools import tee
from statistics import median
from itertools import islice

class PurchasesStats:
    def __init__(self, purchases):
        self.purchases = iter(purchases)
        self.min_price: float = None
        self.max_price: float = None
        self._total_purchases_price: float = 0.0
        self._total_purchases = 0
        self._initialize()

    def _initialize(self):
        try:
            first_value = next(self.purchases)
        except StopIteration:
            raise ValueError("no values provided")

        self.min_price = self.max_price = first_value
        self._update_avg(first_value)

    def process(self):
        for purchase_value in self.purchases:
            self._update_min(purchase_value)
            self._update_max(purchase_value)
            self._update_avg(purchase_value)
        return self

    def _update_min(self, new_value: float):
        if new_value < self.min_price:
            self.min_price = new_value

    def _update_max(self, new_value: float):
        if new_value > self.max_price:
            self.max_price = new_value

    @property
    def avg_price(self):
        return self._total_purchases_price / self._total_purchases

    def _update_avg(self, new_value: float):
        self._total_purchases_price += new_value
        self._total_purchases += 1

    def __str__(self):
        return (
            f"{self.__class__.__name__}({self.min_price}, "
            f"{self.max_price}, {self.avg_price})"
        )


def load_purchases(filename):
    with open(filename) as f:
        for line in f:
            *_, price_raw = line.partition(",")
            yield float(price_raw)


def process_purchases(purchases):
    min_, max_, avg = tee(purchases, 3)
    return min(min_), max(max_), median(avg)


def main():
    create_purchases_file(PURCHASES_FILE)

    purchases = load_purchases(PURCHASES_FILE)
    stats = PurchasesStats(purchases).process()
    logger.info("Results: %s", stats)

    purchases = load_purchases(PURCHASES_FILE)
    obtained = process_purchases(purchases) # itertools의 tee 이용
    logger.info("Obtained: %s", obtained)

    purchases = load_purchases(PURCHASES_FILE)
    purchases = islice(filter(lambda p: p > 1000.0, purchases), 10) # itertools의 islice 이용
    obtained = process_purchases(purchases)
    logger.info("Obtained: %s", obtained)


if __name__ == "__main__":
    main()