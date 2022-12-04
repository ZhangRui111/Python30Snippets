"""
Creates a list of partial sums.
"""
from itertools import accumulate


def accumulated_sum(obj: list):
    return list(accumulate(obj))


print(accumulated_sum([0, 3, 6, 9, 12]))
# >>> [0, 3, 9, 18, 30]

# -------------------- more --------------------
print('-' * 40)

# itertools.accumulate()
#   Syntax: accumulate(iterable[, func]) --> accumulate object
#   Return series of accumulated sums (or other binary function results).

print(list(accumulate([1, 2, 3, 4, 5])))
print(list(accumulate([1, 2, 3, 4, 5], lambda x, y: x * y)))
print(list(accumulate([1, 2, 3, 4, 5], lambda x, y: x - y)))
