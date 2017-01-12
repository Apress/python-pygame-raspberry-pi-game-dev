import pygame, os, sys
from pygame.locals import *

from RobotModel import RobotModel
from RobotView import RobotView
from RadarView import RadarView
from RobotController import RobotController


pygame.init()
fpsClock = pygame.time.Clock()
surface = pygame.display.set_mode((640, 480))	

model = RobotModel((640 - 32) / 2, (480 - 32) / 2, .2)
view = RobotView('robotframes.png')
radarView = RadarView('radar.png', 'blip.png')
controller = RobotController()
		
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
			
	controller.update(fpsClock.get_time() / 1000.0, model)
	
	surface.fill((0, 0, 0))	
	radarView.draw(surface, model)
	view.draw(surface, model)
	
	pygame.display.update()
	fpsClock.tick(30)