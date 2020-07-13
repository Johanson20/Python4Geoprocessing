# landUse.py
# Purpose: Practice performing dictionary operations.
# Usage: No arguments needed.

landUse = {'res': 1, 'com': 2, 'ind': 3, 'other': [4, 5, 6, 7]}
print("Print the value of the item with key 'com'".format(landUse['com']))
if 'res' in landUse.keys():
    val = True
else:
    val = False
print("Check if the dictionary has key 'res': {}".format(val))
landUse['ind'] = landUse['ind'] + 1
print("Increment the value of the item with key 'ind': {}".format(landUse['ind']))
landUse['agr'] = 0
print("Add an item with land use 'agr' a value of 0\n{}".format(landUse))
landUse['res'] = 10
print("Change land use 'res' value to 10.\n{}".format(landUse))
print("Print a list of the dictionary keys:\n{}".format(landUse.keys()))
print('Print the dictionary values:')
for val in landUse.values():
    print(val)
print('Print a list of the dictionary items:')
print(landUse.items())
del(landUse['ind'])
print("Delete the item with key 'ind':\n{}".format(landUse))
if 'ind' in landUse.keys():
    ret = True
else:
    ret = False
print("Check for membership of the key 'ind': {}".format(ret))
