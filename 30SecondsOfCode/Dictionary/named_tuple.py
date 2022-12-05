"""
What are named tuples in Python?
"""
from collections import namedtuple

# Regular tuple
p = (2, 4)  # p[0] = 2, p[1] = 4
print(p[0], p[1])

# Named tuple
Point = namedtuple('Point', ['x', 'y'])  # valid field_names
# Point = namedtuple('Point', 'x y')  # valid field_names
# Point = namedtuple('Point', 'x, y')  # valid field_names
p = Point(2, 4)
print(p.x, p.y)

# -------------------- more --------------------
print('-' * 40)

# 1. the main difference being that values stored in a namedtuple can be
# accessed using field names instead of indexes.
# 2. three ways to assign valid field names
# 3. benefits
#   (1) increased readability
#   (2) default values to be specified (Python >= 3.7)
#   (3) rename=True
#       If you set rename to True, then all the invalid or duplicate field
#       names are automatically replaced with positional names.
#       namedtuple._fields
#   (4) _replace()
#       Since namedtuple is immutable, the values cannot be altered. It
#       returns a new instance by replacing the corresponding keys with
#       a new set of values.

print("The namedtuple with default values:")
ThreeDimsPoint = namedtuple('ThreeDimsPoint', ['x', 'y', 'z'],
                            defaults=[10, 20, 30])
print("demo with 3 defaults")
p = ThreeDimsPoint()
print(p.x, p.y, p.z)
p = ThreeDimsPoint(1)
print(p.x, p.y, p.z)
p = ThreeDimsPoint(1, 2)
print(p.x, p.y, p.z)
# namedtuple has two default values, at least one argument 'x' is required.
ThreeDimsPoint = namedtuple('ThreeDimsPoint', ['x', 'y', 'z'],
                            defaults=[20, 30])
print("demo with 2 defaults")
p = ThreeDimsPoint(1)
print(p.x, p.y, p.z)
p = ThreeDimsPoint(1, 2)
print(p.x, p.y, p.z)
# namedtuple has one default values, at least two argument 'x' & 'y are
# required.
ThreeDimsPoint = namedtuple('ThreeDimsPoint', ['x', 'y', 'z'], defaults=[30])
print("demo with 1 defaults")
p = ThreeDimsPoint(1, 2)
print(p.x, p.y, p.z)

print("The namedtuple with rename=True:")
Point = namedtuple('Point', ['x', 'if', 'class'], rename=True)
print(Point._fields)  # 'if', 'class' are invalid fields
# >>> ('x', '_1', '_2')
Point = namedtuple('Point', ['x', 'if', 'class', 'x'], rename=True)
print(Point._fields)  # the second 'x' is a duplicate field
# >>> ('x', '_1', '_2', '_3')

print("The namedtuple ._replace()")
Point = namedtuple('Point', ['x', 'y'])
p1 = Point(1, 2)
print(p1)
print(id(p1))
p2 = p1._replace(x=10, y=20)  # field names cannot be omitted
print(p2)
print(id(p2))
