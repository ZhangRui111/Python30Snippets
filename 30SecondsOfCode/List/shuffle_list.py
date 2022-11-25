"""
Shuffle list.
"""

# Uses the Fisher-Yates algorithm to reorder the elements of the list.
from copy import deepcopy
from random import randint


def shuffle_list(lst):
    temp_lst = deepcopy(lst)
    m = len(temp_lst)
    while m:
        m -= 1
        i = randint(0, m)  # both 0 & m included
        temp_lst[m], temp_lst[i] = temp_lst[i], temp_lst[m]
    return temp_lst


foo = [1, 2, 3, 4, 5]
print(shuffle_list(foo))


# random.shuffle provides similar functionality to this snippet.
from random import shuffle

foo = [1, 2, 3, 4, 5]
shuffle(foo)  # in-place modification
print(foo)
