import pygame
from pygame.locals import *
from RobotModel import RobotModel

class RadarView:
	
	def __init__(self, radarImagePath, blipImagePath):
		self.radarImg = pygame.image.load(radarImagePath)
		self.blipImg = pygame.image.load(blipImagePath)
		
	def draw(self, surface, model):
		surface.blit(self.radarImg, (0, 0))
		
		x = (model.x / 10.0) + 1
		y = (model.y / 10.0) + 1
		
		surface.blit(self.blipImg, (x, y))