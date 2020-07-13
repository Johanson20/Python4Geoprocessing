# multiwayDict.py
# Purpose: Generate a list of sea level rise (SLR) for each year
#          based on  an IPCC scenario.
# Usage: sea_level_rise_model time_interval
#        SLR should be B1, A1T, B2, A1B, A2, or A1F1;
#        time_interval must be between 1 and 100
# Example input:  AIB 50
import sys

# Input sea level rise model: B1, A1T, B2, A1B, A2, or A1F1
sres= sys.argv[1]

# Input time interval to examine sea level rise
#      (Must be integer between 1 and 100)
interval = int(sys.argv[2])

# Generate a list of sea level rise (SLR) based in the IPCC scenario for each year
rateDict = {'B1': 0.0038, 'A1T': 0.0045, 'B2': 0.0043, 'A1B': 0.0048, 'A2': 0.0051, 'A1F1':0.0059}

if sres in rateDict.keys():
    rate = rateDict[sres]
    sink = []
    b1 = 0
    for year in range(0, 101, interval):
        b1 = b1 + rate*interval
        sink.append(b1)
    print("Running Sea Level Rise Model for {} {}".format(sres, sink))
else:
    print("Warning: Invalid resolution. Choose B1, A1T, B2, A1B, A2, or A1F1.")
