import pygame
from pygame.locals import *
from RobotModel import RobotModel

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