# treeAnalysis.py
# Purpose: Define and use a Tree class to support tree data analysis
# Input: No arguments needed.

### Create a class called Tree
class Tree():
    ### Define an __init__ method.  It should assign 4 properties: block, plot, species, and dbh
    def __init__(self, block, plot, species, dbh):
        '''Initialize tree object properties.'''
        self.block = block
        self.plot = plot
        self.species = species
        self.dbh = dbh

    ### Define a calculateDIB method which returns diameter inside bark (DIB)
    def calculateDIB(self):
        '''Calculate DIB, assuming DIB is diameter breast height times 0.917.'''
        dib = self.dbh*0.917
        return dib

    ### Define a calculateHeight method which returns the tree height
    def calculateHeight(self):
        '''Calculate height, assuming that height is 86.6 plus 0.025 times the
        diameter breast height for loblolly pines (LP)
        and height is 98.8 plus 0.15 times the diameter breast height for all
        other species.'''
        if self.species == 'LP':
            height = 86.6 + 0.025*self.dbh
        else:
            height = 98.8 + 0.15*self.dbh
        return height

    def report(self, num):
        '''Print tree properties.'''
        print('\nReport Tree {}'.format(num))
        print('-------------')
        print('Block: {0}'.format(self.block))
        print('Plot: {0}'.format(self.plot))
        print('Species: {0}'.format(self.species))
        print('DBH: {0}'.format(self.dbh))
        print('DIB: {0}'.format(self.calculateDIB()))
        ### Print the Height as calculated by the calculateHeight method.
        print('Height: {}\n'.format(self.calculateHeight()))


if __name__ == '__main__':
    t1 = Tree(5, 91, 'SG', 14)  # Create a tree object t1 from record 1 of rdu_forest.txt
    print('Tree 1 Species: {}'.format(t1.species))  # Print t1's species.
    dib = t1.calculateDIB()  # Calculate t1's DIB.
    print('Tree 1 DIB: {}'.format(dib))  # Print t1's DIB.
    t1.report(1)  # Report t1 information.

    t2 = Tree(5, 91, 'LP', 23)  # Create a tree object t2 from record 2 of rdu_forest.txt
    ### Print t2's DBH
    print('Tree 2 DBH: {}'.format(t2.dbh))
    ### Calculate t2's height
    height = t2.calculateHeight()
    ### Print t2's height
    print('Tree 2 Height: {}'.format(height))

    ### Create a tree object t3 from record 3 of rdu_forest.txt
    t3 = Tree(5, 91, 'LP', 17)
    ### Print t3's block
    print('Tree 3 block: {}'.format(t3.block))
    ### Print t3's plot
    print('Tree 3 plot: {}'.format(t3.plot))

    ### Create a tree object t4 from record 4 of rdu_forest.txt
    t4 = Tree(5, 91, 'LP', 18)
    ### report t4 information
    t4.report(4)
