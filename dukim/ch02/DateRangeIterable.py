from datetime import timedelta, date


class DateRangeIterable:
    """자체 이터레이터 메서드를 가지고 있는 이터러블"""

    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self._present_day = start_date

    def __iter__(self):
        return self

    def __next__(self):
        if self._present_day >= self.end_date:
            raise StopIteration
        today = self._present_day
        self._present_day += timedelta(days=1)
        return today


if __name__ == '__main__':
    for day in DateRangeIterable(date(2019, 1, 1), date(2019, 1, 5)):
        print(day)

    print("======================")
    r = DateRangeIterable(date(2019, 1, 1), date(2019, 1, 5))
    print(next(r))
    print(next(r))

    print("=====================")
    r1 = DateRangeIterable(date(2019, 1, 1), date(2019, 1, 5))
    print(", ".join(map(str, r1)))
    print("=====================")
    print(max(r1))