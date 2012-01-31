#bin.py

import outcome as o
import unittest as u

class Bin:

    def __init__(self, *outcomes):
       self.outcomes = frozenset(outcomes)
       bin_str = ''

    def add(self, outcome):
        self.outcomes |= set( [outcome] )

    def __str__(self):
        return self.bin_str
        #return ', '.join( map( str, self.outcomes ) )



if __name__ == '__main__':

    four = o.Outcome('4', o.AmericanRouletteOdds.STRAIGHT)
    even = o.Outcome('even', o.AmericanRouletteOdds.EVEN)
    black = o.Outcome('black', o.AmericanRouletteOdds.BLACK)
    street = o.Outcome('street', o.AmericanRouletteOdds.STREET)

    print str(even)
    bin4 = Bin( four, even, black )
    print str(bin4)
    bin4.add(street)
    print str(bin4)




    

    

        
