import numpy
import operator
from CalculateHerf import *
class hSimulation:
	"""Class to handle/store simulation values"""
	
	# Set default values; should not be used, only set to prevent crash if not defined
	
	numberOfFirms = 3
	lstDev = []
	averageFirmSize = 18
	sHerfindahl = {}
	twister = False
	roundval = False
	rState = False
	distNorm = False
	cMS = False
	tLoops = 100
	
	
	# Class Startup, default values defined to prevent crash if undefined
	
	def __init__(self, rState, averageFirmSize=18, lstDev=[], numberOfFirms=3, tLoops=1, twister=True, roundval=False, distNorm=False, cMS=False):
		self.numberOfFirms = numberOfFirms
		self.averageFirmSize = averageFirmSize
		self.lstDev = lstDev
		self.twister = twister
		self.roundval = roundval
		self.rState = rState
		self.distNorm = distNorm
		self.cMS = cMS
		self.tLoops = tLoops

	def getHerfindahl(self):
		return self.sHerfindahl
	
	def Run(self):
		tLoops=self.tLoops
		herfindahlList = []
		for i in range(len(self.lstDev)):
			whileLoopCount = 0
			totalLoopCount = 0
			while (whileLoopCount<tLoops):
				eCg = CalculateHerf(self.rState, self.averageFirmSize, self.lstDev[i], self.numberOfFirms, self.twister)
				herfindahl = float(eCg.GetHerfindahl())
				herfindahlList.append(herfindahl)
				del eCg
				whileLoopCount = whileLoopCount + 1
				totalLoopCount = totalLoopCount + 1
		results = []
		for i in range(11):
			results.append(numpy.percentile(numpy.array(herfindahlList),(i*9.5+2.5)))
		return results
		
		
		