#gamblers_ruin.py

import game as g

r  = g.random.Random()
w = g.wh.Wheel(r)
b = g.wh.BinBuilder()
b.buildBins(w)

t = g.tab.Table(10000)

the_game = g.Game(w, t)

p = g.pl.SimplePlayer(t, w)
b = p.makeMyBet()

for i in xrange(200):
    if p.stake < 20:
        print 'So sad'
        print 'The end'
        break
    the_game.cycle(p, True)
    print p


