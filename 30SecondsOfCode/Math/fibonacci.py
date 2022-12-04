"""
Generates a list, containing the Fibonacci sequence, up until the nth term.
"""


def fibonacci(n: int):
    if n <= 1:
        return [0]

    res = [0, 1]
    for _ in range(2, n):
        res.append(res[-2] + res[-1])
    return res


print(fibonacci(7))
# >>> [0, 1, 1, 2, 3, 5, 8]
print(fibonacci(1))
# >>> [0]
print(fibonacci(2))
# >>> [0, 1]
