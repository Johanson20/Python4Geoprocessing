# MPHzip.py

distanceList = [0.04, 0.05, 0.91, 0.16, 18]
timeList = ['7m:13s', '11m:29s', '16m:48s', '3m:26s', '120m:0s']

motion = zip(distanceList, timeList)
for dist, time in motion:
    minute = int(time.split(':')[0][:-1])
    second = int(time.split(':')[1][:-1])
    hours = float(minute)/60 + float(second)/3600
    speed = dist/hours
    print('Distance: {}\tTime: {}m:{}s\tSpeed: {:.2f} miles/hr'.format(dist, minute, second, speed))
###Hint 1: Inside the 'zip' loop, use several steps to extract the minutes and seconds
###        and then convert to hours.
###Hint 2: To print a float with 2 or less decimal places, put ':.2f' inside the format place holder.
###        Example,
###        >>> speed = 5.1666666666667
###        >>> print 'Speed: {0:.2f} miles/hr'.format(speed)
###        Speed: 5.17 miles/hr
