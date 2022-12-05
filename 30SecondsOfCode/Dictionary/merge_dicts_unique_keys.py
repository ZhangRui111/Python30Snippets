"""
Merges two or more dictionaries with unique keys.
"""


def merge_dictionaries(*dicts):
    merged = dict()
    for dic in dicts:
        merged.update(dic)
    return merged


ages_one = {
  'Peter': 10,
  'Isabel': 11,
}
ages_two = {
  'Anna': 9
}
res = merge_dictionaries(ages_one, ages_two)
print(res)

# -------------------- more --------------------
# dict.update(iterable) method updates the dictionary with the elements from
# another dictionary object or from an iterable of key/value pairs.
# overwrite old value with new value when encountering the same key.

print('-' * 40)

dict_1 = {'A': 'Geeks', 'B': 'For', }
dict_2 = {'B': 'Geeks'}
print(dict_1)
dict_1.update(dict_2)
print(dict_1)
dict_1.update(B='For', C='Geeks')
print(dict_1)
