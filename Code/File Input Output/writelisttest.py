#!/usr/bin/python

# Write out high scores

players = ['Fred,10000', 'Barney,15000', 'Derek,12000', 'Janet,17000']
f = open('highscores.txt', 'w')

for p in players:
	f.write(p + '\n')

f.close()