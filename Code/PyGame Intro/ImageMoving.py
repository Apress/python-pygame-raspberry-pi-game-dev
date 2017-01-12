#!/usr/bin/python

import pygame, sys
from pygame.locals import *

windowSize = (800, 600)

pygame.init()
fpsClock = pygame.time.Clock()

windowSurfaceObj = pygame.display.set_mode(windowSize)
pygame.display.set_caption('Image Example');

image = pygame.image.load('ball.png')
background = pygame.Color(100, 149, 237) # cornflower blue

midX = (windowSurfaceObj.get_width() - image.get_width()) / 2
midY = (windowSurfaceObj.get_height() - image.get_height()) / 2

imgPos = (midX, midY)
speed = (4, 4)

while True:
	
	windowSurfaceObj.fill(background)
	
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
			
			
	newPos = (imgPos[0] + speed[0], imgPos[1] + speed[1])
	
	if (newPos[0] >= windowSurfaceObj.get_width() - image.get_width()):
		newPos = (windowSurfaceObj.get_width() - image.get_width(), newPos[1])
		speed = (speed[0] * -1, speed[1])
		
	if (newPos[0] <= 0):
		newPos = (0, newPos[1])
		speed = (speed[0] * -1, speed[1])
		
	if (newPos[1] >= windowSurfaceObj.get_height() - image.get_height()):
		newPos = (newPos[0], windowSurfaceObj.get_height() - image.get_height())
		speed = (speed[0], speed[1] * -1)
		
	if (newPos[1] <= 0):
		newPos = (newPos[0], 0)
		speed = (speed[0], speed[1] * -1)
		
	imgPos = newPos
	
	windowSurfaceObj.blit(image, imgPos)
			
	pygame.display.update()
	fpsClock.tick(30)