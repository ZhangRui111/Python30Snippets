"""
Chunks a list into smaller lists of a specified size.
"""
from math import ceil


def split_into_chunks_1(obj: list, size: int):
    return [obj[i: i + size] for i in range(0, len(obj), size)]


def split_into_chunks_2(obj: list, size: int):
    return list(map(lambda x: obj[x * size: x * size + size],
                    list(range(ceil(len(obj) / size)))))


print(split_into_chunks_2([1, 2, 3, 4, 5], 2))
# >>> [[1, 2], [3, 4], [5]]
