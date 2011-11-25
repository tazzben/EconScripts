import numpy
from CalculateGamma import *
class gammaSimulation:
	"""Class to handle/store simulation values"""
	
	# Set default values; should not be used, only set to prevent crash if not defined
	
	tranche = []
	numberOfFirms = 3
	lstDev = 1
	averageFirmSize = 18
	sGamma = {}
	sHerfindahl = {}
	sGValue = {} 
	critcalValues = []
	twister = False
	roundval = True
	rState = False
	
	# Class Startup, default values defined to prevent crash if undefined
	
	def __init__(self, rState, averageFirmSize=18, lstDev=1, numberOfFirms=3, tranche=[], critcalValues=[], tLoops=1, twister=False, roundval=True):
		self.tranche = tranche
		self.numberOfFirms = numberOfFirms
		self.averageFirmSize = averageFirmSize
		self.lstDev = lstDev
		self.critcalValues = critcalValues
		self.twister = twister
		self.roundval = roundval
		self.rState = rState
		self.Run(tLoops)

	def getGamma(self):
		return self.sGamma
	
	def getHerfindahl(self):
		return self.sHerfindahl
	
	def getGValue(self):
		return self.sGValue
	
	def Run(self,tLoops):
		gammaList = []
		herfindahlList = []
		gValueList = []
		for i in range(tLoops):
			eCg = CalculateGamma(self.rState,self.averageFirmSize,self.lstDev,self.numberOfFirms,self.tranche,self.twister,self.roundval)
			gamma = float(eCg.GetGamma())
			herfindahl = float(eCg.GetHerfindahl())
			gValue = float(eCg.GetGValue())
			del eCg
			gammaList.append(gamma)
			herfindahlList.append(herfindahl)
			gValueList.append(gValue)
		gammaList.sort()
		self.sGamma = {}
		self.sGamma['mean'] = numpy.mean(gammaList)
		self.sGamma['std'] = numpy.std(gammaList)
		self.sGamma['min'] = numpy.nanmin(gammaList)
		self.sGamma['max'] = numpy.nanmax(gammaList)
		sumProb = float(0)
		sumPValue = float(0)
		gcritcalValues = []
		
		oneUnit = float(1)/float(len(gammaList))
		for i in range(len(self.critcalValues)):
			gcritcalValues.append('')
		for x in range(len(gammaList)):
			if gammaList[x] < 0:
				sumPValue = sumPValue + oneUnit			
			sumProb = sumProb + oneUnit	
			for i in range(len(self.critcalValues)):
				if sumProb < self.critcalValues[i]:
					gcritcalValues[i] = gammaList[x]
		self.sGamma['pvalue'] = sumPValue
		self.sGamma['criticalValues'] = gcritcalValues
		self.sHerfindahl = {}
		self.sHerfindahl['mean'] = numpy.mean(herfindahlList)
		self.sHerfindahl['std'] = numpy.std(herfindahlList)
		self.sHerfindahl['min'] = numpy.nanmin(herfindahlList)
		self.sHerfindahl['max'] = numpy.nanmax(herfindahlList)
		self.sGValue = {}
		self.sGValue['mean'] = numpy.mean(gValueList)
		self.sGValue['std'] = numpy.std(gValueList)
		self.sGValue['min'] = numpy.nanmin(gValueList)
		self.sGValue['max'] = numpy.nanmax(gValueList)
		
		
		