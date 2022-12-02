"""
Creates a dictionary with the unique values of a list as keys and their
frequencies as the values.
"""
from collections import Counter, defaultdict


def frequencies_1(obj: list):
    """ My solution """
    return dict(Counter(obj))


def frequencies_2(obj: list):
    """ My solution """
    freq = defaultdict(int)
    for val in obj:
        freq[val] += 1
    return dict(freq)


print(frequencies_1(['a', 'b', 'a', 'c', 'a', 'a', 'b']))
# >>> {'a': 4, 'b': 2, 'c': 1}
