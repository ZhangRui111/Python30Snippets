"""
Maps a number from one range to another range.
"""


def num_to_range(num, inMin, inMax, outMin, outMax):
    return outMin + ((num - inMin) / (inMax - inMin)) * (outMax - outMin)


print(num_to_range(5, 0, 10, 0, 100))
# >>> 50.0
