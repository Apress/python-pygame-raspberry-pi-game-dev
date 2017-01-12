import pygame, os, sys
from pygame.locals import *

fpsClock = None
bat = None
batRect = None

ball = None
ballRect = None
playerY = 540
ballStartY = 200
ballSpeed = 3
ballServed = False
bx, by = (24, ballStartY)
sx, sy = (ballSpeed, ballSpeed)
brick = None


def init():
	
	global fpsClock

	pygame.init()
	fpsClock = pygame.time.Clock()
	
	surface = pygame.display.set_mode((800, 600))
	pygame.display.set_caption('Bricks');
	backgroundColour = pygame.Color(0, 0, 0)
	
	return (surface, backgroundColour)
	
def loadImage(pathToImg):
	img = pygame.image.load(pathToImg)
	return (img, img.get_rect())
	
def batInit(pathToImg):
	
	global bat
	global batRect
	
	bat, batRect = loadImage(pathToImg)
	
def ballInit(pathToImg):
	
	global ball
	global ballRect
	
	ball, ballRect = loadImage(pathToImg)
	ballRect.topleft = (bx, by)
	
def createBricks(pathToImg, rows, cols):
	
	global brick

	brick = pygame.image.load('brick.png')
	bricks = []

	for y in range(rows):
		brickY = (y * 24) + 100
		
		for x in range(cols):
			brickX = (x * 31) + 245
			bricks.append(Rect(brickX, brickY, brick.get_width(), brick.get_height()))	
	return bricks

mainSurface, black = init()
batInit('bat.png')
ballInit('ball.png')
bricks = createBricks('brick.png', 10, 10)


while True:
	
	ballPrev = (bx, by)
	
	mainSurface.fill(black)

	# brick draw
	for b in bricks:
		mainSurface.blit(brick, b)

	# bat and ball draw
	mainSurface.blit(bat, batRect)
	mainSurface.blit(ball, ballRect)
	
	# events
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == MOUSEMOTION:
			mousex, mousey = event.pos
			if ( mousex < 800 - 55):
				batRect.topleft = (mousex, playerY)
			else:
				batRect.topleft = (800 - 55, playerY)
		elif event.type == MOUSEBUTTONUP:
			if not ballServed:
				ballServed = True
	
	# main game logic 
	if ballServed:
		bx += sx
		by += sy
		ballRect.topleft = (bx, by)
	
	if (by <= 0):
		by = 0
		sy *= -1
		
	if (by >= 600 - 8):
		ballServed = False
		bx, by = (24, ballStartY)
		ballRect.topleft = (bx, by)

	if (bx <= 0):
		bx = 0
		sx *= -1
	
	if (bx >=800 - 8):
		bx = 800 - 8
		sx *= -1
		
	if ballRect.colliderect(batRect):
		by = playerY - 8
		sy *= -1

	# collision detection
	brickHitIndex = ballRect.collidelist(bricks)
	if brickHitIndex >= 0:
		hb = bricks[brickHitIndex]
		
		mx = bx + 4
		my = by + 4
		
		if mx > hb.x + hb.width or mx < hb.x:
			sx *= -1
		else:
			sy *= -1
		
		del (bricks[brickHitIndex])
	
	pygame.display.update()
	fpsClock.tick(30)