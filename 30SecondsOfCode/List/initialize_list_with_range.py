"""
Initializes a list containing the numbers in the specified range where
start and end are inclusive with their common difference step.
"""


def initialize_list_with_range(start, end, step=1):
    return list(range(start, end + 1, step))


print(initialize_list_with_range(0, 5))
# >>> [0, 1, 2, 3, 4, 5]
print(initialize_list_with_range(3, 7, 1))
# >>> [3, 4, 5, 6, 7]
print(initialize_list_with_range(0, 9, 2))
# >>> [0, 2, 4, 6, 8]
