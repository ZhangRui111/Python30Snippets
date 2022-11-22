"""
Builds a list, using an iterator function and an initial seed value.

The iterator function accepts one argument (seed) and must always return
a list with two elements ([value, nextSeed]) or False to terminate.
"""


def unfold(fn, seed):
    def fn_generator(val):
        while True:
            val = fn(val[1])
            if val is False:
                break
            yield val[0]

    return [i for i in fn_generator([None, seed])]


f = lambda n: False if n > 50 else [-n, n + 10]
print(unfold(f, 10))  # [-10, -20, -30, -40, -50]
