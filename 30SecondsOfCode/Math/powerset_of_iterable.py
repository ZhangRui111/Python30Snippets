"""
Returns the powerset of a given iterable.
"""

from itertools import chain, combinations


def powerset(iterable):
    s = list(iterable)
    return list(
        chain.from_iterable(combinations(s, r) for r in range(len(s) + 1)))


print(powerset([1, 2]))
# >>> [(), (1,), (2,), (1, 2)]
print(powerset(['x', 'y', 'z']))
# >>> [(), ('x',), ('y',), ('z',), ('x', 'y'), ('x', 'z'), ('y', 'z'),
#      ('x', 'y', 'z')]

# -------------------- more --------------------
print('-' * 40)

# 1. In mathematics, the power set (or powerset) of a set S is the set of all
#    subsets of S, including the empty set and S itself.
#
# 2. Itertool is a module of Python which is used to creation of iterators
#    which helps us in efficient looping in terms of space as well as time.
#    This module helps us to solve complex problems easily with the help of
#    different sub-functions of itertools.
#
# 3. Itertool.combinations
#    Syntax: combinations(iterable, r) --> combinations object
#    Return successive r-length combinations of elements in the iterable.
print(list(combinations(range(4), 3)))
# >>> (0,1,2), (0,1,3), (0,2,3), (1,2,3)
#
# 4. itertools.chain
#    It is a function that takes a series of iterables and returns one
#    iterable. It groups all the iterables together and produces a single
#    iterable as output.
#    Syntax: chain(*iterables)
#    - chain.from_iterable() function
#      It is similar to chain, but it can be used to chain items from a
#      single iterable, see demo 2
# demo 1
odd = [1, 3, 5, 7, 9]
even = [2, 4, 6, 8, 10]
print(list(chain(odd, even)))
# >>> [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
# demo 2
li = ['ABC', 'DEF', 'GHI', 'JKL']
res1 = list(chain(li))
res2 = list(chain.from_iterable(li))
print("using chain :", res1, end="\n")
print("using chain.from_iterable :", res2)
# >>> using chain : ['ABC', 'DEF', 'GHI', 'JKL']
# >>> using chain.from_iterable : ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
#     'J', 'K', 'L']
