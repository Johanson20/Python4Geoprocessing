# trapezoid.py

def calculateArea(base1, base2, altitude):
    '''Calculate the area of a parallelogram'''
    area = (1/2.0)*altitude*(base1 + base2)
    return area

def isParallelogram(base1, base2):
    '''Check if a geometric figure
        is a parallelogram'''
    if base1 == base2:
        value = True
    else:
        value = False
    return value

def isRectangle(base1, base2, ang):
    '''Check if a geometric figure
        is a rectangle'''
    if isParallelogram(base1, base2) and ang == 90:
        value = True
    else:
        value = False
    return value

def isSquare(base1, base2, altitude, ang):
    '''Check if a geometric figure
        is a square'''
    if isRectangle(base1, base2, ang) and altitude == base1:
        value = True
    else:
        value = False
    return value


# Quad1: b1 = 4, b2 = 4, alt = 6, angle = 90
b1 = 4
b2 = 4
alt = 6
angle = 90

print('Quad1: b1 = 4, b2 = 4, alt = 6, angle = 90')
print('Area = {}'.format(calculateArea(b1, b2, alt)))
print('Is parallelogram? {}'.format(isParallelogram(b1, b2)))
print('Is rectangle? {}'.format(isRectangle(b1, b2, angle)))
print('Is square? {}'.format(isSquare(b1, b2, alt, angle)))
print('')

# Quad2: b1 = 5, b2 = 5, alt = 5, angle = 30
b1 = 5
b2 = 5
alt = 5
angle = 30

print('Quad2: b1 = 5, b2 = 5, alt = 5, angle = 30')
print('Area = {}'.format(calculateArea(b1, b2, alt)))
print('Is parallelogram? {}'.format(isParallelogram(b1, b2)))
print('Is rectangle? {}'.format(isRectangle(b1, b2, angle)))
print('Is square? {}'.format(isSquare(b1, b2, alt, angle)))
print('')

# Quad3: b1 = 8, b2 = 8, alt = 6, angle = 60
b1 = 8
b2 = 8
alt = 6
angle = 60

print('Quad3: b1 = 8, b2 = 8, alt = 6, angle = 60')
print('Area = {}'.format(calculateArea(b1, b2, alt)))
print('Is parallelogram? {}'.format(isParallelogram(b1, b2)))
print('Is rectangle? {}'.format(isRectangle(b1, b2, angle)))
print('Is square? {}'.format(isSquare(b1, b2, alt, angle)))
