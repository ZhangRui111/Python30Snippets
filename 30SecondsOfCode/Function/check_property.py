"""
Creates a function that will invoke a predicate function for the specified
property on a given dictionary.
"""


def check_prop(fn, prop):
    # Return a function with one argument (obj).
    # The role of the function depends on fn & prop.
    return lambda obj: fn(obj[prop])


user = {'name': 'Mark', 'age': 18}
check_age = check_prop(lambda x: x >= 18, 'age')
print(check_age(user))
