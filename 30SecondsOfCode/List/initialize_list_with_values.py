"""
Initializes and fills a list with the specified value.
"""


def initialize_list_with_values(n, val=0):
    return [val for _ in range(n)]


print(initialize_list_with_values(5, 2))
# >>> [2, 2, 2, 2, 2]
