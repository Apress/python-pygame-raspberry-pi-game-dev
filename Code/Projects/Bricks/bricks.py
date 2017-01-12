import pygame, os, sys
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()

windowSurfaceObj = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Arinoids');
whiteColour = pygame.Color(0, 0, 0)

# bat init
bat = pygame.image.load('bat.png')
bat = bat.convert_alpha()
playerY = 540
batRect = bat.get_rect()
mousex, mousey = (24, playerY)

# ball init
ball = pygame.image.load('ball.png')
ball = ball.convert_alpha()
ballRect = ball.get_rect()
ballStartY = 200
ballSpeed = 3
ballServed = False
bx, by = (24, ballStartY)
sx, sy = (ballSpeed, ballSpeed)
ballRect.topleft = (bx, by)

# brick init
brick = pygame.image.load('brick.png')
bricks = []

for y in range(5):
	brickY = (y * 24) + 100
	
	for x in range(10):
		brickX = (x * 31) + 245
		bricks.append((brickX, brickY))

while True:
	
	windowSurfaceObj.fill(whiteColour)

	# brick draw
	for b in bricks:
		windowSurfaceObj.blit(brick, b)
	
	# bat and ball draw
	windowSurfaceObj.blit(bat, batRect)
	windowSurfaceObj.blit(ball, ballRect)
	
	# events
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == MOUSEBUTTONUP:
			if not ballServed:
				ballServed = True
		elif event.type == MOUSEMOTION:
			mousex, mousey = event.pos
			if ( mousex < 800 - 55):
				batRect.topleft = (mousex, playerY)
			else:
				batRect.topleft = (800 - 55, playerY)
	
	# main game logic 
	if ballServed:
		ballRect.topleft = (bx, by)
		bx += sx
		by += sy
	
	if (by >= 640 - 8):
		ballServed = False
		bx, by = (24, ballStartY)
		ballRect.topleft = (bx, by)
		
	if (by <= 0):
		by = 0;
		sy *= -1
		
	if (bx <= 0):
		bx = 0
		sx *= -1
		
	if (bx >=800 - 8):
		bx = 800 - 8
		sx *= -1
	
	# collision detection
	brickForRemoval = None
		
	for b in bricks:
		briX, briY = b
		if ( bx >= briX and bx <= briX + 31):
			if (by >= briY and by <= briY + 16):
				brickForRemoval = b
					
				if (bx <= briX + 2):
					sx *= -1
				elif (bx >= briX + 29):
					sx *= -1
					
				if (by <= briY + 2):
					sy *= -1
				elif (by >= briY + 14):
					sy *= -1
				break
		
	if brickForRemoval <> None:
		bricks.remove(brickForRemoval)
		
	if (bx >= mousex and bx <= mousex + 55):	# bat width = 55. MAGIC NUMBER
		if(by >= playerY - 8 and by <= playerY):
			sy *= -1
			
	pygame.display.update()
	fpsClock.tick(30)