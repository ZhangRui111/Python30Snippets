"""
Filter non-unique list values
"""
from collections import Counter


def filter_non_unique_1(obj: list):
    _obj = set(obj)
    return [i for i in _obj if obj.count(i) == 1]


def filter_non_unique_2(obj: list):
    return [item for item, count in Counter(obj).items() if count == 1]


print(filter_non_unique_2([1, 2, 2, 3, 4, 4, 5]))
# >>> [1, 3, 5]

# -------------------- more --------------------
# Counter is an unordered collection where elements are stored as Dict keys
# and their count as dict value. Although values are intended to be numbers
# but we can store other objects too.

print('-' * 40)

counter = Counter(['a', 'a', 'b'])
print(counter)  # Counter({'a': 2, 'b': 1})
for k, v in counter.items():  # counter.keys()/values()/items()
    print(k, v)


print('-' * 20, '(1)', '-' * 20)
# (1) creat the Counter

# Counter with initial values
counter = Counter(['a', 'a', 'b'])
print(counter)  # Counter({'a': 2, 'b': 1})

# Iterable as argument for Counter
counter = Counter('abc')
print(counter)  # Counter({'a': 1, 'b': 1, 'c': 1})

# List as argument to Counter
words_list = ['Cat', 'Dog', 'Horse', 'Dog']
counter = Counter(words_list)
print(counter)  # Counter({'Dog': 2, 'Cat': 1, 'Horse': 1})

# Dictionary as argument to Counter
word_count_dict = {'Dog': 2, 'Cat': 1, 'Horse': 1}
counter = Counter(word_count_dict)
print(counter)  # Counter({'Dog': 2, 'Cat': 1, 'Horse': 1})

print('-' * 20, '(2)', '-' * 20)
# (2) Ops on the Counter

# Get count
counter = Counter({'Dog': 2, 'Cat': 1, 'Horse': 1})
countDog = counter['Dog']
print(countDog)  # 2
# Get count for non existing key, don't cause KeyError
print(counter['Unicorn'])  # 0

# Set count
counter = Counter({'Dog': 2, 'Cat': 1, 'Horse': 1})
counter['Horse'] = 0
print(counter)  # Counter({'Dog': 2, 'Cat': 1, 'Horse': 0})
# Set count for non-existing key, adds to Counter
counter['Unicorn'] = 1
print(counter)  # Counter({'Dog': 2, 'Cat': 1, 'Unicorn': 1, 'Horse': 0})

# Delete element from Counter
counter = Counter({'Dog': 2, 'Cat': 1, 'Horse': 1})
del counter['Cat']
print(counter)  # Counter({'Dog': 2, 'Horse': 1})

# elements()
counter = Counter({'Dog': 2, 'Cat': 1, 'Horse': -1, 'Unicorn': 0})
elements = counter.elements()  # doesn't return elements with count 0 or less
for value in elements:
    print(value)

# most_common()
# List the n most common elements and their counts from the most common
# to the least.  If n is None, then list all element counts.
counter = Counter({'Cat': 1, 'Dog': 2, 'Horse': -1, 'Unicorn': 0})
most_common_element = counter.most_common()
print(most_common_element)  # [('Dog', 2)]
most_common_element = counter.most_common(1)
print(most_common_element)  # [('Dog', 2)]
most_common_element = counter.most_common(2)
print(most_common_element)  # [('Dog', 2), ('Cat', 1)]
least_common_element = counter.most_common()[:-2:-1]
print(least_common_element)  # [('Horse', -1)]

# subtract() and update()
c1 = Counter('ababab')
print(c1)  # Counter({'a': 3, 'b': 3})
c2 = Counter('abc')
print(c2)  # Counter({'a': 1, 'b': 1, 'c': 1})
# subtract
c1.subtract(c2)
print(c1)  # Counter({'a': 2, 'b': 2, 'c': -1})
# update
c1.update(c2)
print(c1)  # Counter({'a': 3, 'b': 3, 'c': 0})
