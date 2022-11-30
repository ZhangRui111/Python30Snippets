"""
Calculate the binomial coefficient.
"""
from math import comb


def binomial_coefficient(n, k):
    return comb(n, k)


print(binomial_coefficient(8, 2))
# >>> 28

# -------------------- more --------------------
# math.comb()
# math.comb() method in Python is used to get the number of ways to choose
# k items from n items without repetition and without order.
# This method is new in Python version 3.8.
