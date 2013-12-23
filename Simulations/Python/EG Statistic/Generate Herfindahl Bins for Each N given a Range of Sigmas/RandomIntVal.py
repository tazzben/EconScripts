from Crypto.Random import random
import sys
from numpy.random import RandomState
class RandomIntVal:
	
	seed = 1012810
	nState = RandomState(seed)
	cState = random.StrongRandom()
	
	def __init__(self, seed=1012810):
		self.nState = RandomState(seed)
		self.cState = random.StrongRandom()

		# Sampler warmup
		print "Starting Sampler Warm-up"
		junk = self.nState.random_sample(10000)
		print "Warm-up Complete"
	
	def getValue(self):
		maxsize = sys.maxint-1
		rn = float(self.cState.randint(0,maxsize))/maxsize
		return rn
	def getValueTwister(self):
		return self.nState.random_sample()