from EstablishmentOfCohort import *

class CalculateGamma:
	"""Class to calculate gamma value based on a simulated cohort"""

	# Set default values; should not be used, only set to prevent crash if not defined

	cohort = []
	tranche = []
	industrySize = 0
	herfindahlValue = float(0)
	xSquaredSum = float(0)
	siList = []
	gValue = float(0)
	gamma = float(0)
	
	
	# Class Startup, default values defined to prevent crash if undefined
	
	def __init__(self, rState, averageFirmSize=18, lstDev=1, numberOfFirms=3, tranche=[], twister=False, roundval=True):
		self.industrySize = 0
		self.herfindahlValue = float(0)
		self.xSquaredSum = float(0)
		self.gValue = float(0)
		self.gamma = float(0)
		self.tranche = tranche
		self.siList = []
		self.cohort = []
		eCv = EstablishmentOfCohort(rState, averageFirmSize, lstDev, numberOfFirms, self.tranche, twister, roundval)
		self.cohort = eCv.GetFirms()
		del eCv
		
		self.SquaredSumOvertranche()
		self.Herfindahl()
		
		if self.industrySize>0:
			self.DefineSiList()
		else:
			self.siList = [float(0)] * len(self.tranche)
		self.CalculateG()
		self.Calculate()

		
	def GetHerfindahl(self):
		return float(self.herfindahlValue)
		
	def GetGValue(self):
		return float(self.gValue)
		
	def GetGamma(self):
		return float(self.gamma)

	def Calculate(self):
		numerator = self.gValue - float(1)*self.herfindahlValue + self.xSquaredSum*self.herfindahlValue
		oneminus = float(1) - self.herfindahlValue
		denominator = float(1)*oneminus - self.xSquaredSum*oneminus
		if float(denominator) != float(0):
			self.gamma = numerator/denominator
		else:
			self.gamma = float(0)

	def CalculateG(self):
		g = float(0)
		for x in range(len(self.tranche)):
			if x == 0:
				prob = float(self.tranche[0])
			else:
				prob = float(self.tranche[x])-float(self.tranche[x-1])
			gi = float(self.siList[x])-prob
			g = g + gi**2
		self.gValue = g	
	
	def DefineSiList(self):		
		for x in range(len(self.tranche)):
			sumOfi = 0
			for i in range(len(self.cohort)):
				cohortdict = self.cohort[i]
				if cohortdict['tranche'] == x:
					sumOfi = sumOfi + cohortdict['size']
			self.siList.append(float(sumOfi)/float(self.industrySize))
	
	def SquaredSumOvertranche(self):
		sumvalue = float(0)
		for x in range(len(self.tranche)):
			if x == 0:
				prob = float(self.tranche[0])
			else:
				prob = float(self.tranche[x])-float(self.tranche[x-1])
			sumvalue = sumvalue + prob**2
		self.xSquaredSum = sumvalue
	
	def Herfindahl(self):
		size = 0
		for x in range(len(self.cohort)):
			cohortdict = self.cohort[x]
			size = size + float(cohortdict['size'])
		if size == 0:
			return 0
		else:
			self.industrySize = size
		del size
		HValue = float(0)
		if self.industrySize>0:
			for x in range(len(self.cohort)):
				cohortdict = self.cohort[x]
				proportion = float(cohortdict['size'])/float(self.industrySize)
				HValue = HValue + proportion**2
		self.herfindahlValue = HValue