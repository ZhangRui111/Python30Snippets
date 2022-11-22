"""
Creates a flat list of all the keys in a flat dictionary.
"""


def keys_only(obj: dict):
    return list(obj.keys())


ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 9,
}
res = keys_only(ages)
print(res)
# >>> ['Peter', 'Isabel', 'Anna']
