class MyBaseClass(object):
	
	def methodOne(self):
		print "MyBaseClass::methodOne()"
		
class MyChildClass(MyBaseClass):
	
	def methodOne(self):
		print "MyChildClass::methodOne()"
		
class AnotherClass(object):
	
	def methodOne(self):
		print "AnotherClass::methodOne()"

def callMethodOne(obj):
	obj.methodOne()
		

instanceOne = MyBaseClass()
instanceTwo = MyChildClass()
instanceThree = AnotherClass()

callMethodOne(instanceOne)
callMethodOne(instanceTwo)
callMethodOne(5)

