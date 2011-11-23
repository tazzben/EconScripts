from Crypto.Random import random
import sys
class RandomIntVal:
	def getValue(self):
		maxsize = sys.maxint-1
		rn = float(random.randint(0,maxsize))/maxsize
		return rn