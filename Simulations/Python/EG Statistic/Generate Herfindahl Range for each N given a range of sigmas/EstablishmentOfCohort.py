import numpy as np
from scipy.stats import norm
from scipy.stats import lognorm
import math
import logging
class EstablishmentOfCohort:
	"""Class to define cohort of firms for simulation"""
	
	# Set default values; should not be used, only set to prevent crash if not defined
	
	averageFirmSize = 18
	numberOfFirms = 3
	lstDev = 1
	firms = []
	twister = False
	rState = False
	distNorm = False
	roundval = False
	
	# Class Startup, default values defined to prevent crash if undefined
	
	def __init__(self, rState, averageFirmSize, lstDev, numberOfFirms, twister=True, roundval=False, distNorm=False):
		self.averageFirmSize = averageFirmSize
		self.numberOfFirms = numberOfFirms
		self.lstDev = lstDev
		self.twister = twister
		self.roundval = roundval
		self.rState = rState
		self.firms = []
		self.distNorm = False
		for x in range(self.numberOfFirms):
			self.firms.append(self.GetFirmSize())	
	
	def GetFirms(self):
		return self.firms
		
	def GetFirmSize(self):
		if float(self.lstDev) > 0:
			firmsize = np.random.lognormal(self.averageFirmSize, self.lstDev, 1)
			if math.isinf(firmsize) == True:
				firmsize = 0
				logging.info("Infinity encountered")
		else:
			firmsize = self.averageFirmSize
		
		if firmsize > 0:
			return firmsize
		else:
			return 0

	def FindURandom(self):
		if self.twister == True:
			value = self.rState.getValueTwister()
		else:	
			value = self.rState.getValue()
		return value