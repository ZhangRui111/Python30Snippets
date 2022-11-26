"""
How can I check if a string is empty in Python?
"""
# In Python, any object can be tested for truth value, including strings.
# In this context, strings are considered truthy if they are non-empty,
# meaning they contain at least one character. Thus, simply using the not
# operator, you can check if a string is empty.
empty_string = ''
non_empty_string = 'Hello'
print(not empty_string)  # True
print(not non_empty_string)  # False

# more
empty_string = ''
non_empty_string = 'Hello'
non_string = 0
print(not empty_string)  # True
print(not non_empty_string)  # False
print(not non_string)  # True
print(empty_string == '')  # True
print(non_empty_string == '')  # False
print(non_string == '')  # False

