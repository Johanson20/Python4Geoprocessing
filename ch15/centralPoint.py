# centralPoint.py
# Purpose: Use time-related functions to time geoprocessing tool calls.
# Comment: When complete, step through with the DEBUGGER to
#          see non-zero times!!!!
# Usage: input_polygon_shapefile output_directory
# Example script input: C:/gispy/data/ch15/park.shp C:/gispy/scratch/

import datetime, time, sys, arcpy, os


def getTime():
    '''Return a time object for the current time'''
    t = datetime.datetime.now()  # Get a datetime object
    return t  # Return the datetime object to the caller


def timeDifference(start, end, message='Time elapsed:'):
    '''Print a message and the difference between 2 time objects'''
    difference = end - start
    weeks, days = divmod(difference.days, 7)
    minutes, seconds = divmod(difference.seconds, 60)
    hours, minutes = divmod(minutes, 60)
    print(message)
    print('{0} weeks, {1} days, {2}:{3}:{4}'.format(weeks, days, hours,
                                                    minutes, seconds))


infile = sys.argv[1]
outdir = sys.argv[2]
arcpy.env.overwriteOutput = True
arcpy.env.workspace = infile
if not os.path.exists(outdir):
    os.mkdir(outdir)

#calculates time taken to convert polygons to points via centroids
t1 = getTime()
outfile1 = outdir + '/' + os.path.splitext(os.path.basename(infile))[0] + 'Points.shp'
arcpy.FeatureToPoint_management(infile, outfile1)
t2 = getTime()
msg = 'Time for FeatureToPoint to create {}'.format(os.path.basename(outfile1))
timeDifference(t1, t2, msg)

#calculates time taken to find central feature of centroids
t1 = getTime()
outfile2 = outdir + '/' + os.path.splitext(os.path.basename(infile))[0] + 'Central.shp'
arcpy.CentralFeature_stats(outfile1, outfile2, 'EUCLIDEAN_DISTANCE')
t2 = getTime()
msg = 'Time for CentralFeature to create {}'.format(os.path.basename(outfile2))
timeDifference(t1, t2, msg)

#calculates time taken to find the mean centroid
t1 = getTime()
outfile3 = outdir + '/' + os.path.splitext(os.path.basename(infile))[0] + 'Mean.shp'
arcpy.MeanCenter_stats(outfile1, outfile3)
t2 = getTime()
msg = 'Time for MeanCenter to create {}'.format(os.path.basename(outfile3))
timeDifference(t1, t2, msg)

#calculates time taken to estimate distance between central centroid and mean centroid
t1 = getTime()
outfile4 = outdir + '/' + os.path.splitext(os.path.basename(infile))[0] + 'Mean2Central.dbf'
arcpy.PointDistance_analysis(outfile2, outfile3, outfile4)
t2 = getTime()
msg = 'Time for PointDistance to create {}'.format(os.path.basename(outfile4))
timeDifference(t1, t2, msg)
