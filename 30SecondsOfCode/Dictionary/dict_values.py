"""
Returns a flat list of all the values in a flat dictionary.
"""


def values_only(obj: dict):
    return list(obj.values())


ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 9,
}
res = values_only(ages)
print(res)
# >>> [10, 11, 9]
