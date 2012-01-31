
#wheel.py

import bin
import random as r

class Wheel:

    def __init__(self, rng):
        self.rng = rng
        self.all_outcomes = set()
        self.bins = tuple( bin.Bin() for i in xrange(38) )
        self.labelBins()

    def addOutcome(self, number, outcome):
        b = self.get(number)
        b.add( outcome )
        self.all_outcomes.add( outcome )

    def getOutcome( self, name ):
        for oc in self.all_outcomes:
            if oc.name == name:
                return oc

    def spin(self):
        return self.rng.choice( self.bins )

    def randomOutcome(self):
        return self.rng.sample( self.all_outcomes, 1 )[0]

    def get( self, bin ):
    	return self.bins[bin]

    def labelBins( self ):
        for i in xrange(37):
            self.bins[i].bin_str = 'Bin: ' + str(i)

        self.bins[37].bin_str = 'Bin: 00'

    def __str__(self):
        pass


class NonRandom(r.Random):
    def __init__(self):
        pass
    def setSeed(self, value):
        pass
    def choice(self, sequence):
        pass


##### Check this out JR
#####  this is the one I care about
def makeOutcomeString( type, values ):
        if len(values ) > 6:
            val_string = str(values[0]) + '...' + str(values[-1])
        else:
            val_string = '-'.join( map( str, values ) )

        return type + val_string


class BinBuilder:
    def __init__(self):
        pass

    def buildStraightBets(self, w):
        for i in xrange(1, 37):
            out_str = makeOutcomeString( bin.o.RouletteBetType.STRAIGHT, [i] )
            oc = bin.o.Outcome( out_str , bin.o.AmericanRouletteOdds.STRAIGHT )
            w.addOutcome( i, oc )

        out_str = makeOutcomeString( bin.o.RouletteBetType.STRAIGHT, [0] )
        oc = bin.o.Outcome( out_str, bin.o.AmericanRouletteOdds.STRAIGHT )
        w.addOutcome( 0, oc )
        
        out_str = makeOutcomeString( bin.o.RouletteBetType.STRAIGHT, ['00'] )
        oc = bin.o.Outcome( out_str, bin.o.AmericanRouletteOdds.STRAIGHT )
        w.addOutcome( 37, oc )

    def buildSplitBets(self, w):
        for i in xrange(1, 36):
            other_num = i + 1
            values = [i, other_num]
            out_str = makeOutcomeString( bin.o.RouletteBetType.SPLIT, values )
            oc = bin.o.Outcome( out_str, bin.o.AmericanRouletteOdds.SPLIT )
            w.addOutcome( i, oc )
            w.addOutcome( other_num, oc )

        for i in xrange(1, 34):
            other_num = i + 3
            values = [i, other_num]
            out_str = makeOutcomeString( bin.o.RouletteBetType.SPLIT, values )
            oc = bin.o.Outcome( out_str, bin.o.AmericanRouletteOdds.SPLIT )
            w.addOutcome( i, oc )
            w.addOutcome( other_num, oc )

    def buildStreetBets(self, w):
        for i in xrange(12):
            num1 = 3*i + 1
            num2 = 3*i + 2
            num3 = 3*i + 3
            values = [num1, num2, num3]
            out_str = makeOutcomeString( bin.o.RouletteBetType.STREET, values )
            oc = bin.o.Outcome( out_str, bin.o.AmericanRouletteOdds.STREET )
            w.addOutcome( num1, oc )
            w.addOutcome( num2, oc )
            w.addOutcome( num3, oc )

    def buildLineBets(self, w):
        for i in xrange(11):
            values = [ 3*i + x for x in xrange(1, 7) ]
            out_str = makeOutcomeString( bin.o.RouletteBetType.LINE, values )
            oc = bin.o.Outcome( out_str, bin.o.AmericanRouletteOdds.LINE )
            for j in values:
                w.addOutcome( j, oc )
  
 
    def buildColumnBets(self, w):
        for i in [1, 2, 3]:
            values = [ 3*x + i for x in xrange(12) ]
            out_str = makeOutcomeString( bin.o.RouletteBetType.COLUMN, values )
            oc = bin.o.Outcome( out_str, bin.o.AmericanRouletteOdds.COLUMN )
            for j in values:
                w.addOutcome( j, oc )
                
    def buildDozenBets(self, w):
        for i in [0, 1, 2]:
            values = [ 12*i + x for x in xrange(1, 13) ]
            out_str = makeOutcomeString( bin.o.RouletteBetType.RANGE, values )
            oc = bin.o.Outcome( out_str, bin.o.AmericanRouletteOdds.RANGE )
            for j in values:
                w.addOutcome( j, oc )
 

    def buildEvenMoneyBets(self, w):
        values = bin.o.RouletteNums.RED
        out_str = makeOutcomeString( bin.o.RouletteBetType.RED, values )
        oc = bin.o.Outcome( out_str, bin.o.AmericanRouletteOdds.RED )
        for j in bin.o.RouletteNums.RED:
            w.addOutcome( j, oc )
        
        values = bin.o.RouletteNums.BLACK
        out_str = makeOutcomeString( bin.o.RouletteBetType.BLACK, values )
        oc = bin.o.Outcome( out_str, bin.o.AmericanRouletteOdds.BLACK )
        for j in bin.o.RouletteNums.BLACK:
            w.addOutcome( j, oc )

        values = bin.o.RouletteNums.EVEN
        out_str = makeOutcomeString( bin.o.RouletteBetType.EVEN, values )
        oc = bin.o.Outcome( out_str, bin.o.AmericanRouletteOdds.EVEN )
        for j in values:
            w.addOutcome( j, oc )
        
        values = bin.o.RouletteNums.ODD
        out_str = makeOutcomeString( bin.o.RouletteBetType.ODD, values )
        oc = bin.o.Outcome( out_str, bin.o.AmericanRouletteOdds.ODD )
        for j in values:
            w.addOutcome( j, oc )

        values = bin.o.RouletteNums.LOW
        out_str = makeOutcomeString( bin.o.RouletteBetType.LOW, values )
        oc = bin.o.Outcome( out_str, bin.o.AmericanRouletteOdds.LOW )
        for j in values:
            w.addOutcome( j, oc )
    
        values = bin.o.RouletteNums.HIGH
        out_str = makeOutcomeString( bin.o.RouletteBetType.HIGH, values )
        oc = bin.o.Outcome( out_str, bin.o.AmericanRouletteOdds.HIGH )
        for j in values:
            w.addOutcome( j, oc )
   

    def buildBins( self, wheel ):
        self.buildStraightBets( wheel )
        self.buildSplitBets( wheel )
        self.buildStreetBets( wheel )
        self.buildColumnBets( wheel )
        self.buildDozenBets( wheel )
        self.buildLineBets( wheel )
        self.buildEvenMoneyBets( wheel )



if __name__ == '__main__':
    r = r.Random()
    ww = Wheel(r)
    b = BinBuilder()
    b.buildBins(ww)

    values = bin.o.RouletteNums.HIGH
    out_str = makeOutcomeString( bin.o.RouletteBetType.HIGH, values )
    oc = ww.getOutcome(out_str)
    print oc

    print oc in ww.all_outcomes

    for i in xrange(4):
       b = ww.spin()
       # print b
       # print oc in b.outcomes

    # print ww.get(37)





