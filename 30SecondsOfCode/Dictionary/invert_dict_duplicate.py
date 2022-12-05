"""
Inverts a dictionary with non-unique hashable values.
"""
from collections import defaultdict


def invert_dictionary(obj: dict):
    # create a defaultdict with the values that are list.
    inv_obj = defaultdict(list)
    for key, value in obj.items():
        inv_obj[value].append(key)
    return dict(inv_obj)


ages = {
    'Peter': 10,
    'Isabel': 10,
    'Anna': 9,
}
inverted = invert_dictionary(ages)
print(inverted)
# >>> { 10: ['Peter', 'Isabel'], 9: ['Anna'] }

# -------------------- more --------------------
print('-' * 40)

# Dictionary in Python is an unordered collection of data values that
# are used to store data values like a map.
# The functionality of both dictionary and defaultdict are almost same
# except for the fact that defaultdict never raises a KeyError. It
# provides a default value for the key that does not exists.


def def_value():
    """ Function to return a default values for keys that is not present """
    return "Not Present"


# Defining the dict
print("defaultdict d1:")
d1 = defaultdict(def_value)
d1["a"] = 1
d1["b"] = 2
print(d1["a"])
print(d1["b"])
print(d1["c"])
print("defaultdict d2:")
d2 = defaultdict(lambda: "Not Present")
d2["a"] = 1
d2["b"] = 2
print(d2["a"])
print(d2["b"])
print(d2["c"])
print("defaultdict d3:")
d2 = defaultdict(int)  # create a defaultdict with default value as zero.
d2["a"] += 1
print(d2["a"])
