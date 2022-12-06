"""
Understanding Python's slice assignment
"""

# Slice assignment has the same syntax as slicing a list with the only
# exception that it's used on the left-hand side of an expression instead
# of the right-hand side. Since slicing returns a list, slice assignment
# requires a list (or other iterable).

# print("Slice assignment without changing length")

nums = [1, 2, 3, 4, 5]

nums[:1] = [6]        # [6, 2, 3, 4, 5]   (replace elements 0 through 1)
nums[1:3] = [7, 8]    # [6, 7, 8, 4, 5]   (replace elements 1 through 3)
nums[-2:] = [9, 0]    # [6, 7, 8, 9, 0]   (replace the last 2 elements)

# We can use slice assignment to replace part of the list with a different
# list whose length is also different from the returned slice.

# print("Slice assignment that changes length")

nums = [1, 2, 3, 4, 5]

nums[1:4] = [6, 7]         # [1, 6, 7, 5]        (replace 3 elements with 2)
nums[-1:] = [8, 9, 0]      # [1, 6, 7, 8, 9, 0]  (replace 1 element with 3)
nums[:1] = []              # [6, 7, 8, 9, 0]     (replace 1 element with 0)

# If you take empty slices into account, you can also insert elements into
# a list without replacing anything in it. For example:

nums = [1, 2, 3, 4, 5]

nums[2:2] = [6, 7]    # [1, 2, 6, 7, 3, 4, 5]   (insert 2 elements)
nums[7:] = [8, 9]     # [1, 2, 6, 7, 3, 4, 5, 8, 9] (append 2 elements)
nums[:0] = [0]        # [0, 1, 2, 6, 7, 3, 4, 5, 8, 9] (prepend 1 element)
nums[:] = [4, 2]     # [4, 2] (replace whole list with a new one)

# Step is also applicable in slice assignment. If step is not 1, the inserted
# list must have the exact same length as that of the returned list slice,
# i.e., we cannot change the length. Like slice notation, the direction of
# slice assignment depends on the sign of the step, i.e., negative step means
# slice assignment in reverse.

print("Slice assignment with non-one step")

try:
    nums = [1, 2, 3, 4, 5]
    nums[2:0:-1] = [11]
    print(nums)
except ValueError as e:
    print("ValueError: {}".format(e))  # ValueError
try:
    nums = [1, 2, 3, 4, 5]
    nums[2:0:-1] = [11, 22, 33]
    print(nums)
except ValueError as e:
    print("ValueError: {}".format(e))  # ValueError
try:
    nums = [1, 2, 3, 4, 5]
    nums[2:0:-1] = [11, 22]
    print(nums)  # [1, 22, 11, 4, 5]
except ValueError as e:
    print("ValueError: {}".format(e))
try:
    nums = [1, 2, 3, 4, 5]
    nums[2::2] = [6, 7, 8]
    print(nums)
except ValueError as e:
    print("ValueError: {}".format(e))  # ValueError
try:
    nums = [1, 2, 3, 4, 5]
    nums[-2:-5:-1] = [22, 33, 44]
    print(nums)  # [1, 44, 33, 22, 5]
except ValueError as e:
    print("ValueError: {}".format(e))
try:
    nums = [1, 2, 3, 4, 5]
    nums[1::-1] = [11, 22]
    print(nums)  # [22, 11, 3, 4, 5]
except ValueError as e:
    print("ValueError: {}".format(e))
