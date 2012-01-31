#player.py


import table as tab

class Player:
    def __init__( self, table ):
        self.name = ''
        self.stake = 0
        self.table = table
        self.player_bets = []

    def isPlaying(self):
        return True
        
    def processWin( self, bet ):
        self.stake += bet.winAmount() + bet.amount
        if bet in self.player_bets:
            self.player_bets.remove(bet)
        
    def processLose( self, bet ):
        if bet in self.player_bets:
            self.player_bets.remove(bet)

    def placeBets( self ):
        pass

    def __str__(self):
        return  '%s:    $%d' % ( self.name, self.stake )
  

class SimplePlayer(Player):
    def __init__( self, table, wheel ):
        Player.__init__(self, table)
        self.stake = 500
        self.wheel = wheel
        self.name = 'Roger'

    def makeMyBet(self):
        oc = self.wheel.randomOutcome()
        amount = 20
        return tab.bet.Bet( amount, oc )

 
    def placeBets( self ):
        b = self.makeMyBet()
        if b.amount == 0: return
        if b.amount <= self.stake:
            self.stake -= b.amount
            self.table.receiveBet(b)
            self.player_bets.append(b)


if __name__ == '__main__':
    t = tab.Table(1000)
    p = SimplePlayer(t)
    b = p.makeMyBet()
    print b
