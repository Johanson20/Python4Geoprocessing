# tideRecords.py
# Purpose: Practice performing dictionary operations.
# Usage: No arguments needed.

tides = {'G1': [1, 6], 'G2': [2], 'G3': [3, 8, 9]}
tides['G5'] = [2]
print(tides)
tides['G5'].append(6)
print(tides)
tides['G3'].pop()
print(tides)
tides['G6'] = []
print(tides)
del(tides['G3'])
print(tides)
g1Correct = [val/float(2) for val in tides['G1']]
tides['G1'] = g1Correct
print(tides)
