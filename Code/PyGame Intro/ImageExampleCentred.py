#!/usr/bin/python

import pygame
from pygame.locals import *

windowSize = (800, 600)

pygame.init()
fpsClock = pygame.time.Clock()

windowSurfaceObj = pygame.display.set_mode(windowSize)
pygame.display.set_caption('Image Example');

image = pygame.image.load('townscape.jpg')
background = pygame.Color(100, 149, 237) # cornflower blue

imgPos = ((800 - 640)/2, (600 - 480)/2)

while True:
	
	windowSurfaceObj.fill(background)
	
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
			
			
	windowSurfaceObj.blit(image, imgPos)
			
	pygame.display.update()
	fpsClock.tick(30)