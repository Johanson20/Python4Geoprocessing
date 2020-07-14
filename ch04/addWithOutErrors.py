# addWithErrors.py
# Purpose: Demonstrate exceptions within a script
# What the script should do when fixed:
#             add two numbers given as arguments.

# Import sys, so that the script can use this module.
import sys

# Get the 1st user argument. Cast it to float.
a = float(sys.argv[1])
# Get the 2nd user argument. Cast it to float too.
b = float(sys.argv[2])
c = a + b
print("The sum is {0}.".format(c))
