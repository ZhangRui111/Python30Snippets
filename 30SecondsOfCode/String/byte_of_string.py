"""
Returns the length of a string in bytes.
"""


def byte_size(s):
    # print(s.encode('utf-8'))
    return len(s.encode('utf-8'))


print(byte_size('😀'))  # 4
print(byte_size('Hello World'))  # 11
