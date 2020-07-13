# add_version2.py multiplies any two numbers entered by the user.

# int changes the input to an integer number.
a = input('Enter first integer: ')
b = input('Enter second integer: ')

c = a * b
# format(c) substitutes the value of c for {0} in the print statement.
print 'The product of {1} and {2} is {0}.'.format(c,a,b)
