from EstablishmentOfCohort import *
from decimal import *

class CalculateGamma:
	"""Class to calculate gamma value based on a simulated cohort"""

	# Set default values; should not be used, only set to prevent crash if not defined

	cohort = []
	tranche = []
	industrySize = 0
	herfindahlValue = Decimal(0)
	xSquaredSum = Decimal(0)
	siList = []
	gValue = Decimal(0)
	gamma = Decimal(0)
	
	
	# Class Startup, default values defined to prevent crash if undefined
	
	def __init__(self, averageFirmSize=18, lstDev=1, numberOfFirms=3, tranche=[]):
		self.tranche = tranche
		eCv = EstablishmentOfCohort(averageFirmSize, lstDev, numberOfFirms, self.tranche)
		self.cohort = eCv.GetFirms()
		del eCv
		
		self.SquaredSumOvertranche()
		self.Herfindahl()
		
		if self.industrySize>0:
			self.DefineSiList()
		else:
			self.siList = [Decimal(0)] * len(self.tranche)
		self.CalculateG()
		self.Calculate()


		
	def GetHerfindahl(self):
		return float(self.herfindahlValue)
		
	def GetGValue(self):
		return float(self.gValue)
		
	def GetGamma(self):
		return float(self.gamma)

	def Calculate(self):
		numerator = self.gValue - Decimal(1)*self.herfindahlValue + self.xSquaredSum*self.herfindahlValue
		oneminus = Decimal(1) - self.herfindahlValue
		denominator = Decimal(1)*oneminus - self.xSquaredSum*oneminus
		if Decimal(denominator) != Decimal(0):
			self.gamma = numerator/denominator
		else:
			self.gamma = Decimal(0)

	def CalculateG(self):
		g = Decimal(0)
		for x in range(len(self.tranche)):
			if x == 0:
				prob = Decimal(str(self.tranche[0]))
			else:
				prob = Decimal(str(self.tranche[x]))-Decimal(str(self.tranche[x-1]))
			gi = Decimal(str(self.siList[x]))-prob
			g = g + gi**2
		self.gValue = g	
	
	def DefineSiList(self):		
		for x in range(len(self.tranche)):
			sumOfi = 0
			for i in range(len(self.cohort)):
				cohortdict = self.cohort[i]
				if cohortdict['tranche'] == x:
					sumOfi = sumOfi + cohortdict['size']
			self.siList.append(Decimal(sumOfi)/Decimal(self.industrySize))
	
	def SquaredSumOvertranche(self):
		sumvalue = Decimal(0)
		for x in range(len(self.tranche)):
			if x == 0:
				prob = Decimal(str(self.tranche[0]))
			else:
				prob = Decimal(str(self.tranche[x]))-Decimal(str(self.tranche[x-1]))
			sumvalue = sumvalue + prob**2
		self.xSquaredSum = sumvalue
	
	def Herfindahl(self):
		size = 0
		for x in range(len(self.cohort)):
			cohortdict = self.cohort[x]
			size = size + Decimal(cohortdict['size'])
		if size == 0:
			return 0
		else:
			self.industrySize = size
			del size
		HValue = Decimal(0)
		if self.industrySize>0:
			for x in range(len(self.cohort)):
				cohortdict = self.cohort[x]
				proportion = Decimal(cohortdict['size'])/Decimal(self.industrySize)
				HValue = HValue + proportion**2
		self.herfindahlValue = HValue