#!/usr/bin/python

# Draw box with params

def drawBox(width = 3, height = 3):
	
	if width < 0:
		width = 3
		
	if height < 3:
		height = 3
		
	width = width - 2
		
	print "+" + "-" * width + "+"
	
	for y in range(3, height + 1):
		print "|" + " " * width + "|"	
	
	print "+" + "-" * width + "+"
	
print "5x4"
drawBox(5, 4)

print "4x3"
drawBox(4)

print "3x4"
drawBox(height=4)
