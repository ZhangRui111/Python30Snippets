"""
Chunks a list into n smaller lists.
"""
from math import ceil


def split_into_n_chunks_1(obj: list, num: int):
    size = ceil(len(obj) / num)
    return [obj[i: i + size] for i in range(0, len(obj), size)]


def split_into_n_chunks_2(obj: list, num: int):
    size = ceil(len(obj) / num)
    return list(map(lambda x: obj[x * size: x * size + size],
                    list(range(num))))


print(split_into_n_chunks_2([1, 2, 3, 4, 5, 6, 7], 4))
# >>> [[1, 2], [3, 4], [5, 6], [7]]
