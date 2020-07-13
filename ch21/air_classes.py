# Author:   Johanson Onyegbula
# Usage:    Creates airline, flight and seat objects for the manipulation
#           of airline operations

import datetime, math, time

seats = []
##

class Airline():
    def __init__(self, airname, flightID):
        '''Initializes an airline object'''
        self.name = airname
        self.flightID = flightID

    def BookFlight(self, flyID):
        '''Assign a flight for the airline'''
        return Flight(flyID, self.name)

    def CancelFlight(self, flyID):
        '''Cancel an already book flight'''
        if flyID in flightID:
            flightID.remove(flyID)
        else:
            print("Flight {} hasn't been booked.".format(flyID))

    def NumberOfFlights(self):
        '''Calculate number of flights per day for an airline'''
        return len(self.flightID)


class Flight():
    '''Initialize a flight object'''
    def __init__(self, flightID, airline, seats=[80,4]):
        self.flightID = flightID
        self.name = airline
        self.seats = seats

##    def AssignSeat(self):
##        '''Assign seats to a plane'''
##        if self.flyType == 'Arik':
##            noSeats = 300
##        elif self.flyType == 'Emirates':
##            noSeats = 375
##        else:
##            noSeats = 250
##        return noSeats

    def BookSeat(self, seatID):
        '''Book a seat in a flight'''
        if seatID[0] in range(1, 1+self.seats[0]) and seatID[1] in range(1, 1+self.seats[1]):
            return Seat(seatID, self.flightID)
        else:
            print('Seat {} is beyond flight capacity and cannot be booked.'.format(seatID))
##        val = '{};{}'.format(aa.CostOfSeat(), seatID)
##        valu = val.split(';')[1]
##        if len(seats) > 0 and valu in seats[0].split(';')[1]:
##            print('''Reservation status of new booking {}: {}
##Seat already previously booked! Kindly book a free seat.\n'''.format(aa.seatID, aa.SeatStatus()))
##            del(aa)
##        else:
##            seats.append(val)
##            print('Reserved seat number {} for you!\n'.format(aa.seatID))
##            return aa

    def LoadFactor(self):
        loadfact = 0.5 * (self.FlightCapacity/(float(self.seats[0]*self.seats[1])))
        return loadfact

    def LengthOfFlight(self, oriAir, destAir):
        '''Calculate flight length based on coordinates
        of departure and destination airports'''
        dx = destAir[0] - oriAir[0]
        dy = destAir[1] - oriAir[1]
        flightLen = math.sqrt(dx**2 + dy**2)
        return flightLen

    def TimeOfFlight(self, depTime, arriTime):
        '''Calculate time of flight given arrival
        and departure time as lists containing a list
        of 6 time properties containing year, month,
        day, hour, minute and second'''
        flyTime = datetime.datetime(depTime) - datetime.datetime(arriTime)
        return flyTime.seconds

    def FlightCapacity(self):
        '''Determine flight capacity'''
        return len(seats)

    def TotalFlightFare(self):
        '''Calculate total cost of flight fare'''
        total = [cost.fare for cost in seats]
        return sum(total)


class Seat():
    def __init__(self, seatID, flightID, fare=0, status='Vacant', classO=''):
        '''Initialize a seat object'''
        self.seatID = seatID
        self.fare = fare
        self.flightID = flightID
        self.status = status
        self.classO = classO

        self.ClassOfSeat()
        if len(seats) > 0 and self.seatID in [seat.seatID for seat in seats]:
            self.status = 'Occupied'
            print('''Reservation status of new booking {}: {}
Seat already previously booked! Kindly book a free seat.\n'''.format(self.status, self.seatID))
            del(self)
        else:
            seats.append(self)
            print('Reservation made: Seat {1} is {0} and costs ${2}.\n'.format(self.ClassOfSeat(), self.seatID, self.fare))

    def ClassOfSeat(self):
        '''Determine class of a seat'''
        if self.seatID[0] <= 5:
            seatclass = 'First Class'
            self.fare = 100
        elif self.seatID[0] <= 15:
            seatclass = 'Business Class'
            self.fare = 55
        else:
            seatclass = 'Economy Class'
            self.fare = 25
        return seatclass

    def ModifySeat(self, newID):
        self.seatID = newID


if __name__=='__main__':
    #create airline objects
    air1 = Airline('Johanson', [7, 1, 4])

    #book a flight on Arik air with flight number 4
    flight1 = air1.BookFlight(4)
    #Book a seat on row 141, column 2
    mySeat = flight1.BookSeat([71, 2])
    mySeat2 = flight1.BookSeat([141, 2])

    #book more seats on same flight
    seat2 = flight1.BookSeat([1,1])
    seat1 = flight1.BookSeat([3,2])
    seat3 = flight1.BookSeat([2,1])
    seat4 = flight1.BookSeat([8,1])

    #print total flight fare, length and capacity
    print('Total flight capacity is {}'.format(flight1.FlightCapacity()))
    print('Total flight fare is ${}'.format(flight1.TotalFlightFare()))
    print('Flight distance is {:.3f}km.'.format(flight1.LengthOfFlight([40000, 851,795], [675,021, 310,000])))
