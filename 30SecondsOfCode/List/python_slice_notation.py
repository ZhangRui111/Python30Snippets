"""
Understanding Python's slice notation
"""

# Basic syntax: obj[start_at:stop_before:step]
# the default values are start_at = 0, stop_before = len(nums), step = 1.

print("Basic syntax")

nums = [1, 2, 3, 4, 5]

print(nums[1:4])     # [2, 3, 4] (start at 0, stop before 4)
print(nums[2:])      # [3, 4, 5] (start at 0, stop at end of list)
print(nums[:3])      # [1, 2, 3] (start at 0, stop before 3)
print(nums[1:4:2])   # [2, 4] (start at 1, stop before 4, every 2nd element)
print(nums[2::2])    # [3, 5] (start at 2, stop at end of list, every 2nd element)
print(nums[:3:2])    # [1, 3] (start at 0, stop before 3, every 2nd element)
print(nums[::2])     # [1, 3, 5] (start at 0, stop at end of list, every 2nd element)
print(nums[::])      # [1, 2, 3, 4, 5] (start at 0, stop at end of list)

# An idiomatic way to shallow clone a list would be using [:]
# (e.g. nums_clone = nums[:]).

print("Shallow clone")

nums_clone = nums[:]
print(nums_clone)

# All three of the arguments also accept negative values. For start_at and
# stop_before, a negative value means counting from the end of the list
# instead of counting from the start. For example -1 would represent the last
# element, -2 the second last element etc. Note that -0 equals to 0, and -0
# does not count from the end. For example:

print("Negative values")

nums = [1, 2, 3, 4, 5]

print(nums[1:-2])    # [2, 3] (start at 1, stop before 2nd to last)
print(nums[-3:-1])   # [3, 4] (start at 3rd to last, stop before last)
print(nums[-0:-1])   # [1, 2, 3, 4] (start at 0, stop before last)

# A negative step means that the list is sliced in reverse (from end to start).
# This also means that start_at should be greater than stop_before and that
# stop_before in the context of a reverse stride is more like stop_after if you
# are looking at the list non-reversed. For example:

print(nums[::-1])     # [5, 4, 3, 2, 1] (reversed)
print(nums[4:1:-1])   # [5, 4, 3] (reversed, start at 4, stop after 1)
print(nums[-1:1:-2])  # [5, 3] (reversed, start at last, stop after 1, every 2nd)

# Slice notation is very forgiving, so you'll get an empty list if the
# arguments' values are out of the list's range.

print("Empty slices")

nums = [1, 2, 3, 4, 5]

print(nums[6:8])     # []
print(nums[:-10])    # []
