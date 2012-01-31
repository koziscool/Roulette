#table.py

import bet

class Table:

    def __init__(self, bet_limit):
        self.bet_limit = bet_limit
        self.table_bets = []

    def __iter__(self):
        return iter( self.table_bets ) 

    def isValid(self, bet):
        if bet.amount <= self.BetLimit:
    	   return True
        else: return False

    def receiveBet(self, bet):
        self.table_bets.append( bet )

    def clearBets(self):
        self.table_bets = []

    def __str__(self):
        return ', '.join( map( str, self.table_bets ) )


    
