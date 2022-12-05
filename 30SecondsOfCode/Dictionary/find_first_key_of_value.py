"""
Finds the first key in the provided dictionary that has the given value.
"""


def find_first_key_of_value(obj: dict, val):
    return next(k for k, v in obj.items() if v == val)


ages = {
    'Peter': 10,
    'Isabel': 11,
    'Tom': 11,
    'Anna': 9,
    'Jerry': 11,
}
res = find_first_key_of_value(ages, 11)
print(res)
# >>> 'Isabel'

# -------------------- more --------------------
print('-' * 40)

# 1. iterator and the StopIteration


def find_key_of_value_iterator(obj: dict, val):
    return (k for k, v in obj.items() if v == val)


it = iter(find_key_of_value_iterator(ages, 11))
a = next(it)
while a:
    print(a)
    try:
        a = next(it)
    except StopIteration:
        a = False  # important!

# 2. comprehension and the original order
# set comprehension does not guarantee the original order
# dict/list/tuple comprehension guarantee the original order
print('-' * 40)
a_set = {k for k, v in ages.items() if v == 11}
print(a_set)
# sorted results in a consistent order but not necessarily the original order
a_set_sorted = sorted({k for k, v in ages.items() if v == 11})
print(a_set_sorted)
a_dict = {k: v for k, v in ages.items() if v == 11}
print(a_dict)
a_list = [k for k, v in ages.items() if v == 11]
print(a_list)
a_tuple = tuple(k for k, v in ages.items() if v == 11)
print(a_tuple)
