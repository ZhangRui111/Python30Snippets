"""
Converts a list of dictionaries into a list of values corresponding to
the specified key.
"""


def pluck_values_1(obj: list, key: str):
    return list(map(lambda item: item[key], obj))


def pluck_values_2(obj: list, key: str):
    return [dic.get(key) for dic in obj]


simpsons = [
    {'name': 'lisa', 'age': 8},
    {'name': 'homer', 'age': 36},
    {'name': 'marge', 'age': 34},
    {'name': 'bart', 'age': 10}
]
print(pluck_values_1(simpsons, 'age'))
print(pluck_values_2(simpsons, 'age'))
# >>> [8, 36, 34, 10]
