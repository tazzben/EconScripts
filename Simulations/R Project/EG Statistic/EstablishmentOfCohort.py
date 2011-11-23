import numpy as np
from scipy.stats import norm
from decimal import *
from RandomIntVal import *
class EstablishmentOfCohort:
	"""Class to define cohort of firms for simulation"""
	
	# Set default values; should not be used, only set to prevent crash if not defined
	
	averageFirmSize = 18
	numberOfFirms = 3
	tranche = []
	lstDev = 1
	firms = []
	
	# Class Startup, default values defined to prevent crash if undefined
	
	def __init__(self, averageFirmSize=18, lstDev=1, numberOfFirms=3, tranche=[]):
		self.averageFirmSize = averageFirmSize
		self.numberOfFirms = numberOfFirms
		self.lstDev = lstDev
		self.tranche = tranche
		
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
		firmsize = np.round(np.exp(norm.ppf(float(self.FindURandom()),scale=float(self.lstDev),loc=np.log(float(self.averageFirmSize)))))
		if firmsize > 0:
			return firmsize
		else:
			return 0

	def FindURandom(self):
		rIV = RandomIntVal()
		value = rIV.getValue()
		del rIV
		return value