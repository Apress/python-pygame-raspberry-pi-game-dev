import pygame
from pygame.locals import *
from RobotModel import RobotModel

class RobotView:
	
	def __init__(self, imgPath):
		self.img = pygame.image.load(imgPath)
		
	def draw(self, surface, model):
		src = Rect(model.frame * 32, 0, 32, 32)
		surface.blit(self.img, (model.x, model.y), src)