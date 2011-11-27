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
	tranche = []
	lstDev = 1
	firms = []
	twister = False
	rState = False
	distNorm = False
	
	# Class Startup, default values defined to prevent crash if undefined
	
	def __init__(self, rState, averageFirmSize=18, lstDev=1, numberOfFirms=3, tranche=[], twister=False, roundval=True, distNorm=False):
		self.averageFirmSize = averageFirmSize
		self.numberOfFirms = numberOfFirms
		self.lstDev = lstDev
		self.tranche = tranche
		self.twister = twister
		self.roundval = roundval
		self.rState = rState
		self.firms = []
		self.distNorm = False
		
		for x in range(self.numberOfFirms):
			firmDict = {}
			firmDict['tranche'] = self.Findtranche()
			firmDict['size'] = self.GetFirmSize()
			self.firms.append(firmDict)	
	
	def GetFirms(self):
		return self.firms
	
	def Findtranche(self):
		randomValue = self.FindURandom()
		for x in range(len(self.tranche)):
			if randomValue < self.tranche[x]:
				return x
		return x
	
	def GetFirmSize(self):
		if float(self.lstDev) > 0:
			if self.distNorm==True:
				firmsize = float(norm.ppf(float(self.FindURandom()),scale=float(self.lstDev),loc=float(self.averageFirmSize)))
			else:
				firmsize = float(lognorm.ppf(float(self.FindURandom()),float(self.lstDev)/float(self.averageFirmSize),scale=float(self.averageFirmSize)))
			if math.isinf(firmsize) == True:
				firmsize = 0
				logging.info("Infinity encountered")
		else:
			firmsize = self.averageFirmSize
		if self.roundval==True:
			firmsize = np.round(firmsize)
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