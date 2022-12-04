"""
Returns a random element from a list.
"""
import random


def sample(obj: list):
    return random.choice(obj)


print(sample([3, 7, 9, 11]))

# -------------------- more --------------------
print('-' * 40)

# 1. random.choice() returns a random item from a list, tuple, or string.
#    Syntax:
#      random.choice(sequence)
# 2. random.choices() returns multiple random elements from the list with
#    replacement. You can weigh the possibility of each result with the weights
#    parameter or the cum_weights parameter. The elements can be a string, a
#    range, a list, a tuple or any other kind of sequence.
#    Syntax:
#      random.choices(sequence, weights=None, cum_weights=None, k=1)
print(random.choices(["apple", "banana", "mango"], weights=[10, 1, 1], k=6))
# 3. returns a particular length list of items chosen from the sequence, i.e.,
#    list, tuple, string or set. Used for random sampling without replacement.
#    Syntax:
#      random.sample(sequence, k)
#        If the sample size i.e. k is larger than the sequence size, ValueError
#        is raised.
print(random.sample([1, 2, 3, 4, 5], 3))
