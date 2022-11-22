"""
Finds all keys in the provided dictionary that have the given value.
"""


def find_keys_with_value(obj: dict, val):
    return [k for k, v in obj.items() if v == val]


ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 10,
}
res = find_keys_with_value(ages, 10)
print(res)
# >>> ['Peter', 'Anna']
