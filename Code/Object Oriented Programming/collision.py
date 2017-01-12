class Alien:
	
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
	def draw(self):
		pass
		
class AlienSwarm:
	
	def __init__(self, numAliens):
		self.swarm = []
		
		y = 0
		x = 24
		
		for n in range(numAliens):
			alien = Alien(x, y)
			self.swarm.append(alien)
			
			x += 24
			if x > 640:
				x = 0
				y += 24
				
	def debugPrint(self):
		for a in self.swarm:
			print "x=%d, y=%d" % (a.x, a.y)

	def isHit(self, x, y):
		alienToRemove = None
		for a in self.swarm:
			if x>=a.x and x <= a.x + 24 and y >= a.y and y <= a.y + 24:
				alienToRemove = a
				break
				
		if alienToRemove != None:
			self.swarm.remove(alienToRemove)
			return True
			
		return False
			
class Player:
	
	def __init__(self):
		self.bullets = []
		
	def getBullets(self):
		return self.bullets
		
	def removeBullet(self, bullet):
		self.bullets.remove(bullet)
		
class Collision:
	
	def __init__(self, player, swarm):
		self.player = player
		self.swarm = swarm
		
	def checkCollisions(self):
		
		bulletKill = []
		
		for b in player.getBullets():
			if swarm.isHit(b.x, b.y):
				bulletKill.append(b)
				continue
				
		for b in bulletKill:
			self.player.score += 10
			self.player.removeBullet(b)
		
swarm = AlienSwarm(5)
player = Player()

collision = Collision(player, swarm)
collision.checkCollisions()