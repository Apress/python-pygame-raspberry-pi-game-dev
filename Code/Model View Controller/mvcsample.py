import pygame, os, sys
import random
from pygame.locals import *


class RobotModel:
	
	def __init__(self, x, y, speed):
		self.x = x
		self.y = y
		self.frame = 0
		self.pixelsPerSec = 200
		self.speed = speed
		self.clock = speed
		
class RadarView:
	
	def __init__(self, radarImagePath, blipImagePath):
		self.radarImg = pygame.image.load(radarImagePath)
		self.blipImg = pygame.image.load(blipImagePath)
		
	def draw(self, surface, model):
		surface.blit(self.radarImg, (0, 0))
		
		x = (model.x / 10.0) + 1
		y = (model.y / 10.0) + 1
		
		surface.blit(self.blipImg, (x, y))
		

class RobotView:
	
	def __init__(self, imgPath):
		self.img = pygame.image.load(imgPath)
		
	def draw(self, surface, model):
		src = Rect(model.frame * 32, 0, 32, 32)
		surface.blit(self.img, (model.x, model.y), src)
		
class RobotController:
	
	def update(self, deltaTime, model):
		model.clock -= deltaTime
		if (model.clock < 0):
			model.clock += model.speed
			model.frame += 1
			model.frame %= 2
			
		keys = pygame.key.get_pressed()
		
		if (keys[K_RIGHT]):
			model.x += model.pixelsPerSec * deltaTime
		elif (keys[K_LEFT]):
			model.x -= model.pixelsPerSec * deltaTime
			
		if (keys[K_UP]):
			model.y -= model.pixelsPerSec * deltaTime
		elif (keys[K_DOWN]):
			model.y += model.pixelsPerSec * deltaTime
			
		if (model.x <= 0):
			model.x = 0
			
		if (model.x >= 640 - 32):
			model.x = 640 - 32
			
		if (model.y <= 0):
			model.y = 0
			
		if (model.y >= 480 - 32):
			model.y = 480 - 32			
	

pygame.init()
fpsClock = pygame.time.Clock()
surface = pygame.display.set_mode((640, 480))	

model = RobotModel((640 - 32) / 2, (480 - 32) / 2, .2)
view = RobotView('robotframes.png')
controller = RobotController()

radarView = RadarView('radar.png', 'blip.png')
		
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
			
	controller.update(fpsClock.get_time() / 1000.0, model)
	
	surface.fill((0, 0, 0))	
	view.draw(surface, model)
	radarView.draw(surface, model)
			
	pygame.display.update()
	fpsClock.tick(30)
	
		
		
		