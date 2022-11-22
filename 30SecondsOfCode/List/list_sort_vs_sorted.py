"""
What is the difference between list.sort() and sorted() in Python?

Differences:
    1. list.sort() will sort the list in-place, mutating its indexes and
       returning None, whereas sorted() will return a new sorted list leaving
       the original list unchanged.
    2. sorted() accepts any iterable object (e.g. list, tuple, dictionary,
       string), while list.sort() is a method of the list class and can only be
       used with lists.

In common:
Both list.sort() and sorted() have the same key and reverse optional arguments.
"""
nums = [2, 3, 1, 5, 6, 4, 0]

print(sorted(nums))
print(nums)

print(nums.sort())
print(nums)

# -------------------- more --------------------

# keyword: reverse
# reverse - If True, the sorted list is reversed (or sorted in Descending order)
print("-" * 40)

nums = [2, 3, 1, 5, 6, 4, 0]

print(sorted(nums, reverse=True))
print(nums)

print(nums.sort(reverse=True))
print(nums)

# keyword: key
# key - A function that serves as a key for the sort comparison
print("-" * 40)

lst = ['ccccc', 'dddd', 'bbbbbb', 'ff', 'g', 'eee', 'aaaaaa']
print(lst.sort(key=len))
print(lst)

dicts = {'c': 4, 'd': 3, 'b': 5, 'f': 1, 'g': 0, 'e': 2, 'a': 6}
print(dict(sorted(dicts.items(), key=None)))
print(dicts)

dicts = {'c': 4, 'd': 3, 'b': 5, 'f': 1, 'g': 0, 'e': 2, 'a': 6}
print(dict(sorted(dicts.items(), key=lambda item: item[1])))
print(dicts)

dicts = {'c': 4, 'd': 3, 'b': 5, 'f': 1, 'g': 0, 'e': 2, 'a': 6}
print(dict(sorted(dicts.items(), key=lambda item: - item[1])))
print(dicts)
