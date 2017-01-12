#!/usr/bin/python

num = 5

def printNum():
	global num
	num = 10
	print num
	
printNum()
print num