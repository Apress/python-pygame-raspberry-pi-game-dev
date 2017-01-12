
class RobotModel:
	
	def __init__(self, x, y, speed):
		self.x = x
		self.y = y
		self.frame = 0
		self.pixelsPerSec = 200
		self.speed = speed
		self.clock = speed