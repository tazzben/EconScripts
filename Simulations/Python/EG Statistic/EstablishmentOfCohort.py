import numpy as np
from scipy.stats import norm
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
	
	# Class Startup, default values defined to prevent crash if undefined
	
	def __init__(self, rState, averageFirmSize=18, lstDev=1, numberOfFirms=3, tranche=[], twister=False, roundval=True):
		self.averageFirmSize = averageFirmSize
		self.numberOfFirms = numberOfFirms
		self.lstDev = lstDev
		self.tranche = tranche
		self.twister = twister
		self.roundval = roundval
		self.rState = rState
		
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
		firmsize = np.exp(norm.ppf(float(self.FindURandom()),scale=float(self.lstDev),loc=np.log(float(self.averageFirmSize))))
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