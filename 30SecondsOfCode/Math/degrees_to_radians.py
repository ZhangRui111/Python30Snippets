"""
Converts an angle from degrees to radians.
"""
from math import pi


def degrees_to_rads(deg):
    return (deg * pi) / 180.0


print(degrees_to_rads(180))
# >>> 3.141592653589793
