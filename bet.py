#bet.py

import wheel as wh

class Bet(object):
    def __init__( self, amount, outcome ):
        self.amount = amount
        self.outcome = outcome

    def winAmount(self):
        return self.outcome.odds * self.amount
    
    def loseAmount(self):
        return self.amount

    def __eq__(self, other):
        return self.outcome == other.outcome and self.amount == other.amount

    def __ne__(self, other):
        return self.outcome != other.outcome or self.amount != other.amount

    def __str__(self):
        return "$%d (%s)" % ( self.amount, self.outcome )

if __name__ == '__main__':

    r = wh.r.Random()
    ww = wh.Wheel(r)

    b = wh.BinBuilder()
    b.buildBins(ww)

    nums = wh.bin.o.RouletteNums.RED
    oc_str = wh.makeOutcomeString( wh.bin.o.RouletteBetType.RED, nums )
    oc = ww.getOutcome(oc_str)
 
    b = Bet( 20, oc )
    print str(b)
