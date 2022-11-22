"""
Tip: You should use dict.get(key) instead of dict[key]
"""
# dict.get() is usually preferred, as it accepts a second argument which
# acts as the default value shall the key not exist in the given dictionary.
# Due to this property, dict.get() will always return a value, whereas
# dict[key] will raise a KeyError if the given key is missing.


a = {'max': 200}
b = {'min': 100, 'max': 250}
c = {'min': 50}

try:
    res = a['min'] + b['min'] + c['min']
except KeyError as err_info:
    print("throws KeyError")
    print(err_info)
else:
    print(res)

res = a.get('min', 0) + b.get('min', 0) + c.get('min', 0)
print(res)
