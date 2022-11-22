"""
Inverts a dictionary with unique hashable values.
"""


def invert_dictionary(obj: dict):
    return {val: key for key, val in obj.items()}


ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 9,
}
res = invert_dictionary(ages)
print(res)
# >>> {10: 'Peter', 11: 'Isabel', 9: 'Anna'}
