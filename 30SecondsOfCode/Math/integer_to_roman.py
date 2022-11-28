"""
Converts an integer to its roman numeral representation. Accepts value
between 1 and 3999 (both inclusive).
"""


def integer_to_roman_numeral(num):
    lookup = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I'),
    ]
    res = ''
    for (n, roman) in lookup:
        (d, num) = divmod(num, n)
        res += roman * d
    return res


print(integer_to_roman_numeral(3))  # 'III'
print(integer_to_roman_numeral(11))  # 'XI'
print(integer_to_roman_numeral(1998))  # 'MCMXCVIII'
print(integer_to_roman_numeral(2998))  # 'MMCMXCVIII'

# -------------------- more --------------------
# divmod(x, y): Return the tuple (x//y, x%y).
