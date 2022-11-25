"""
What is the difference between lists and tuples in Python?
"""

# Lists
#   - Syntax: [1, 2, 3]
#   - Contained elements are mutable (can be changed after creation)
#   - Lists have a variable length
#   - A list takes up more memory than a tuple
# Tuples
#   - Syntax: (1, 2, 3)
#   - Contained elements are immutable (cannot be changed after creation)
#   - Tuples have a fixed length
#   - A tuple takes up less memory than a list
#
# When to use each one
#   Lists provide a more accessible API and should be used whenever similar
#   types of objects need to be stored and are expected to change over the
#   course of the application's execution. On the other hand, tuples should
#   be used for immutable data, behaving more like constants than variables.
