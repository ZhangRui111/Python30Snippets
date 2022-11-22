"""
Converts a list of dictionaries into a list of values corresponding to
the specified key.
"""


def pluck_values(obj: list, key: str):
    return [dic.get(key) for dic in obj]


simpsons = [
    {'name': 'lisa', 'age': 8},
    {'name': 'homer', 'age': 36},
    {'name': 'marge', 'age': 34},
    {'name': 'bart', 'age': 10}
]
res = pluck_values(simpsons, 'age')
print(res)
