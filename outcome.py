#outcome.py

class RouletteBetType:
    STRAIGHT = 'Straight: '
    SPLIT = 'Split: '
    STREET = 'Street: '
    CORNER = 'Corner: '
    LINE = 'Line: '
    FIVE =  'Five: '
    RANGE = 'Range: '
    COLUMN = 'Column: '
    HIGH = 'High: '
    LOW = 'Low: '
    EVEN = 'Even: '
    ODD = 'Odd: '
    BLACK = 'Black: '
    RED = 'Red: '

class AmericanRouletteOdds:
    STRAIGHT = 35
    SPLIT = 17
    STREET = 11
    CORNER = 8
    LINE = 5
    FIVE = 6
    RANGE = 2
    COLUMN = 2
    HIGH = 1
    LOW = 1
    EVEN = 1
    ODD = 1
    BLACK = 1
    RED = 1

class RouletteNums:
    RED = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36 ]
    BLACK = [ 2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35 ]

    EVEN = [i for i in xrange(1, 37) if i%2 == 0]
    ODD = [i for i in xrange(1, 37) if i%2 != 0]

    LOW = [i for i in xrange(1, 19)]
    HIGH = [i for i in xrange(19, 37)]
 

class Outcome(object):

    def __init__( self, name , odds ):
        self.name = name
        self.odds = odds
 
    def __eq__(self, other):
        return self.name == other.name

    def __ne__(self, other):
        return self.name != other.name

    def winAmount(self, amount):
        return self.odds * amount

    def __str__(self):
        return "%s (%d:1)" % ( self.name, self.odds )

    
# import unittest as u

# class TestOutcome(u.TestCase):

#     def __init__(self):
#         self.koz, self.cool = 2, 9

#     def testA(self):
#         assert self.koz == self.koz

#     def testB(self):
#         assert self.koz == self.cool


if __name__ == '__main__':

    #t = TestOutcome()

    koz = Outcome('yyy', 11)
    cool = Outcome('yyy', 35)

    print koz == cool
    
    #u.main() 
