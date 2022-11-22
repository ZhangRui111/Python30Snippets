"""
Retrieves the value of the nested key indicated by the given selector
list from a dictionary or list.
"""
from functools import reduce
from operator import getitem


def get_nested_value_by_key_0(dic: dict, keys: list):
    """ A recursion solution """
    if len(keys) == 1:
        return dic[keys[0]]
    return get_nested_value_by_key_0(dic[keys.pop(0)], keys)


def get_nested_value_by_key_1(dic: dict, keys: list):
    """ A reduce solution """
    return reduce(getitem, keys, dic)


users = {
  'freddy': {
    'name': {
      'first': 'fred',
      'last': 'smith'
    },
    'postIds': [1, 2, 3]
  }
}

print(get_nested_value_by_key_0(users, ['freddy', 'name']))
print(get_nested_value_by_key_0(users, ['freddy', 'name', 'last']))
print(get_nested_value_by_key_0(users, ['freddy', 'postIds', 1]))
print(get_nested_value_by_key_1(users, ['freddy', 'name']))
print(get_nested_value_by_key_1(users, ['freddy', 'name', 'last']))
print(get_nested_value_by_key_1(users, ['freddy', 'postIds', 1]))

# -------------------- more --------------------
print('-' * 40)
# 1. reduce()
#    reduce(function, iterable, initializer=None)
#    arguments:
#      function -- function with two arguments
#      iterable -- iterable object
#      initializer -- initial params, optional
#    (1) The reduce(fun, seq) function is used to apply a particular function
#        passed in its argument to all of the list elements mentioned in the
#        sequence passed along.
#        - At first step, first two elements of sequence are picked and the
#          result is obtained.
#        - Next step is to apply the same function to the previously attained
#          result and the number just succeeding the second element and the
#          result is again stored.
#        - This process continues till no more elements are left in the
#          container.
#        - The final returned result is returned and printed on console.
#    (2) The reduce(fun, seq, ini) places the 3rd parameter before the value
#        of the second one, if it's present.

print(reduce(lambda x, y: x + y, [1, 2, 3, 4]))
print(reduce(lambda x, y: x + y, [1, 2, 3, 4], 10))


# Python program to  illustrate sum of two numbers.
def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value

# 2. getitem(a, b) is the same as a[b]
