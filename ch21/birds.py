#-------------------------------------------------------------------------------
# Name:        birds.py
# Purpose:     Creates a bird class that's imported by famousBirds script
#
# Author:      Johanson Onyegbula
#-------------------------------------------------------------------------------

class Bird():
    def __init__(self, name, habitat, weight):
        '''Initialize bird object properties'''
        self.name = name
        self.habitat = habitat
        self.weight = weight

    def talk(self):
        '''Print out sound made by bird'''
        if self.name == 'Toucan':
            print('Squawk!')
        else:
            print('Tweet')

    def diet(self):
        '''Define diet of bird based on geography'''
        if self.habitat == 'South America':
            result = 'fruit'
        elif self.habitat == 'North America':
            result = 'bugs'
        else:
            result = 'fish'
        return result


if __name__ == '__main__':
    bigBird = Bird('Condor', 'Sesame Street', 2000)
    bigBird.talk()
    bigBird.talk()
    bigBird.talk()
    food = bigBird.diet()
    print('{} eats {}.'.format(bigBird.name, food))
