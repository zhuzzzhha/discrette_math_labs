from tkinter import *

def convertFromDecimalToAny(num, base, upper=False):
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    if base > len(digits): return None
    result = ''
    number = int(num)
    while number > 0:
        result = digits[number % base] + result
        number //= base
    return str(result.upper()) if upper else result


def convertFromAnyToDecimal(num, bas):
    number = str(num)
    base = int(bas)
    return str(int(number, base))

print(convertFromDecimalToAny('123', 7))
print(convertFromAnyToDecimal('0b11001', 2))



