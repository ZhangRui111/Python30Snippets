"""
Converts an angle from radians to degrees.
"""
from math import pi


def rads_to_degrees(rad):
    return (rad * 180.0) / pi


print(rads_to_degrees(pi / 2))
# >>> 90.0
