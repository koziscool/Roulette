
#game.py

import wheel as wh
import player as pl
import random
import table as tab


class Game:
    def __init__( self, wheel, table ):
        self.wheel = wheel
        self.table = table

    def getBets(self, player):
        if player.isPlaying():
            new_bets = player.placeBets()
        
    def spin(self, wheel):
        self.current_bin = self.wheel.spin()

    def displayBetsAndResults(self):
        for b in self.table:
            print 'Bet: ', b, '  result is ', self.current_bin

    def resolveBets( self, player ):
        for b in self.table:
            if b.outcome in self.current_bin.outcomes:
                player.processWin(b)
            else:
                player.processLose(b)
        self.table.clearBets()

    def cycle( self, player, display = False ):
        self.getBets(player)
        self.spin(self.wheel)
        if display:
            self.displayBetsAndResults()
        self.resolveBets(player)


    
if __name__ == '__main__':
    r  = random.Random()
    w = wh.Wheel(r)
    b = wh.BinBuilder()
    b.buildBins(w)

    t = tab.Table(10000)

    g = Game(w, t)

    p = pl.SimplePlayer(t, w)
    b = p.makeMyBet()

    for i in xrange(12):
        g.cycle(p, True)
        print p

