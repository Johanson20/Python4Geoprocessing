# moduloTry.py
# Purpose: Compute the remainder of dividing two numbers.
# Usage: Two integer values
# Example input1: 25 4
# Example input2: 5 0
# Example input3: woods 3

import sys

field1 = sys.argv[1]
field2 = sys.argv[2]
print("a: {0}   b: {1}".format(field1, field2))
try:
    a = int(field1)
    b = int(field2)
    c = a % b
except ZeroDivisionError:
    c = '{} mod {} is undefined'.format(a, b)
except ValueError:
    print('Usage: <numeric value 1> <numeric value 2>')
    c = 'Not found'
print("c:", c)
