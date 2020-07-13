# tideRecordsLoop.py
# Purpose: Practice performing dictionary operations.
# Usage: No arguments needed.
tides = {'G1': [1, 6], 'G2': [2], 'G3': [3, 8, 9]}
for ind in tides.keys():
    tides[ind].append(7)
print(tides)
for val in tides.values():
    print('Number of readings: {}'.format(len(val)))
for ind, values in tides.items():
    adjVal = [v**2 for v in values]
    tides[ind] = adjVal
print(tides)
for ind, values in tides.items():
    print('Minimum reading at guage {} = {}'.format(ind, min(values)))
