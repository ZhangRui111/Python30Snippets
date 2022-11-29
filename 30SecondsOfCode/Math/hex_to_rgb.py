"""
Converts a hexadecimal color code to a tuple of integers corresponding to
its RGB components.
"""


def hex_to_rgb(hex: str):
    return tuple(int(hex[i:i + 2], base=16) for i in (0, 2, 4))


rgb = hex_to_rgb('FFA501')  # (255, 165, 1)
print(rgb)

# -------------------- more --------------------
# 1. The hexadecimal color code is corresponding to its RGB channels
# 2. int(obj, base=10)  # base must be >= 2 and <= 36, or 0
#    Python int() function Return decimal (base-10) representation of x.
