engine=0		# A global variable is created

class car(object):		# The class is created. It works as a code-base that can be used for any car created.
	
	def __init__(self,kmh):		# A constructor is created. It will only be run once, when the code is
		self.speed=kmh		# started, and you can insert default values here.
	
	def start(self):		# A function is created
		global engine		
		print "The engine is running"	
		engine=1

	def increase(self):		# A function is created
		if engine==1:	
			self.speed=self.speed+20
			print "Going in " + str(self.speed)
		else:
			print "Start the engine first!"

	def decrease(self):		# A function is created
		if engine==1:
			self.speed=self.speed-20
			print "Going in " + str(self.speed)
		else:
			print "Start the engine first!"

	def stop(self):			# A function is created
		global engine		
		self.speed=0
		print "The car has stopped"
		engine=0

mycar=car(0)			# A car is created and given a default speed value
mycar.increase()		#  \
mycar.start()			#  |
mycar.increase()		#  |
mycar.increase()		#   \__Here the different functions will be run in the order listed.
mycar.decrease()		#   /  The functions will only affect "mycar".
mycar.decrease()		#  |
mycar.stop()			#  |
mycar.decrease()		#  /
