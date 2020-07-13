# enumList.py
# Purpose: Use the enumerate function in a FOR-loop (instead of the WHILE-loop)
# Usage: No arguments needed.

fieldNames = ['earth', 'wind', 'fire']

# original code:
index = 0
for index, files in enumerate(fieldNames):
    print('Field {0} is {1}.'.format(index, files))
