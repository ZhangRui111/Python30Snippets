"""
Initializes a 2D list of given width and height and value.
"""


def initialize_2d_list(width, height, val=None):
    return [[val for i in range(width)] for j in range(height)]


print(initialize_2d_list(2, 2, 0))
# >>> [[0, 0], [0, 0]]

# -------------------- more --------------------
# Initializes a 3D list


def initialize_3d_list(width, height, depth, val=None):
    return [[[val for i in range(width)] for j in range(height)]
            for k in range(depth)]

print(initialize_3d_list(2, 2, 2, 0))
# >>> [[[0, 0], [0, 0]], [[0, 0], [0, 0]]]
