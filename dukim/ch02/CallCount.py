from collections import defaultdict


class CallCount:

    def __init__(self):
        self._counts = defaultdict(int)

    def __call__(self, argument):
        self._counts[argument] += 1
        return self._counts[argument]


cc = CallCount()
print(cc(1))
print(cc(1))
print(cc(2))
print(cc(2))
print(cc(3))
print(cc(2))
