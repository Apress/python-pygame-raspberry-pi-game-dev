#!/usr/bin/python

# Draw box with params

def drawBox(width, height):
	
	if width < 0:
		width = 3
		
	if height < 3:
		height = 3
		
	width = width - 2
		
	print "+" + "-" * width + "+"
	
	for y in range(3, height + 1):
		print "|" + " " * width + "|"	
	
	print "+" + "-" * width + "+"
	

drawBox(5, 4)