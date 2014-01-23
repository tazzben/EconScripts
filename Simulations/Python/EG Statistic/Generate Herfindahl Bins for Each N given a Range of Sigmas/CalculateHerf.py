from EstablishmentOfCohort import *

class CalculateHerf:
	"""Class to calculate gamma value based on a simulated cohort"""

	# Set default values; should not be used, only set to prevent crash if not defined

	cohort = []
	industrySize = 0
	herfindahlValue = float(0)
	
	
	# Class Startup, default values defined to prevent crash if undefined
	
	def __init__(self, rState, averageFirmSize, lstDev, numberOfFirms, twister=True, roundval=False, distNorm=False, cMS = False):
		self.industrySize = 0
		self.herfindahlValue = float(0)
		self.cohort = []
		eCv = EstablishmentOfCohort(rState, averageFirmSize, lstDev, numberOfFirms, twister, roundval, distNorm)
		
		self.cohort = eCv.GetFirms()
		del eCv		
		self.Herfindahl()
				
	def GetHerfindahl(self):
		return float(self.herfindahlValue)
	
	def Herfindahl(self):
		size = 0
		for x in range(len(self.cohort)):
			cohortdict = self.cohort[x]
			size = size + float(cohortdict)
		if size == 0:
			return 0
		else:
			self.industrySize = size
		del size
		HValue = float(0)
		if self.industrySize>0:
			for x in range(len(self.cohort)):
				cohortdict = self.cohort[x]
				proportion = float(cohortdict)/float(self.industrySize)
				HValue = HValue + proportion**2
		self.herfindahlValue = HValue