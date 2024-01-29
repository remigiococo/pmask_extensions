import random
from pmask.exception import *
from pmask.generator import *

class WalkList(Generator):
	def __init__(self, list):
		Generator.__init__(self)
		if len(list) == 0:
			raise TooFewElements
		self.list = list
		self.index = int( random.random() * len(list) )

	def valueAt(self, evaluationTime):
		r = random.random()
		step = 1
		if( r < 0.5 ):
			step = -1
		self.index += step
		if( self.index >= len(self.list) ):
			self.index -= 1;
		if( self.index < 0 ):
			self.index += 1;
		return self.list[ self.index ]
