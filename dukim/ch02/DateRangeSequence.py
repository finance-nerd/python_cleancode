from datetime import timedelta, date


class DateRangeSequence:
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self._range = self._create_range()

    def _create_range(self):
        days = []
        current_day = self.start_date
        while current_day < self.end_date:
            days.append(current_day)
            current_day += timedelta(days=1)
        return days

    def __getitem__(self, day_no):
        return self._range[day_no]
    def __len__(self):
        return len(self._range)

if __name__ == '__main__':
    s1 = DateRangeSequence(date(2019, 1, 1), date(2019, 1, 5))
    for day in s1:
        print(day)

    print("=====================")
    print(s1[0])