import numpy
import operator
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
	roundval = False
	rState = False
	distNorm = False
	pValues = []
	cMS = False
	
	# Class Startup, default values defined to prevent crash if undefined
	
	def __init__(self, rState, averageFirmSize=18, lstDev=1, numberOfFirms=3, tranche=[], critcalValues=[], tLoops=1, twister=False, roundval=False, distNorm=False, pValues=[], cMS=False):
		self.tranche = tranche
		self.numberOfFirms = numberOfFirms
		self.averageFirmSize = averageFirmSize
		self.lstDev = lstDev
		self.critcalValues = critcalValues
		self.twister = twister
		self.roundval = roundval
		self.rState = rState
		self.distNorm = distNorm
		self.pValues = pValues
		self.cMS = cMS
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
		combindedList = []
		for i in range(tLoops):
			eCg = CalculateGamma(self.rState,self.averageFirmSize,self.lstDev,self.numberOfFirms,self.tranche,self.twister,self.roundval,self.distNorm, self.cMS)
			gamma = float(eCg.GetGamma())
			herfindahl = float(eCg.GetHerfindahl())
			gValue = float(eCg.GetGValue())
			del eCg
			gammaList.append(gamma)
			herfindahlList.append(herfindahl)
			gValueList.append(gValue)
			combined = {}
			combined['gamma'] = gamma
			combined['herfindahl'] = herfindahl
			combindedList.append(combined)
		gammaList.sort()
		herfindahlList.sort()
		combindedList.sort(key=operator.itemgetter('gamma'))
		
		self.sGamma = {}
		self.sGamma['mean'] = numpy.mean(gammaList)
		self.sGamma['std'] = numpy.std(gammaList)
		self.sGamma['min'] = numpy.nanmin(gammaList)
		self.sGamma['max'] = numpy.nanmax(gammaList)
		sumProb = float(0)
		finalPValue = float(0)
		gcritcalValues = []
		gpvalueList = []
		hvlist = []
		hcritcalValues = []
		hatcrit = []
		hatcritl = []
		hatcrits = []
		hatcritls = []
		herflist = []
		
		oneUnit = float(1)/float(len(gammaList))
		
		for i in range(len(self.pValues)):
			gpvalueList.append('')
		
		for i in range(len(self.pValues)):
			hvlist.append('')

		for i in range(len(self.critcalValues)):
			hcritcalValues.append('')
		
		for i in range(len(self.critcalValues)):
			gcritcalValues.append('')
			hatcrit.append('')
			hatcritl.append('')
			hatcrits.append('')
			hatcritls.append('')
		
		
		for x in range(len(gammaList)):
						
			sumProb = sumProb + oneUnit	
			
			
			if gammaList[x] < 0:
				finalPValue = sumProb
				
			for i in range(len(self.pValues)):
				if gammaList[x] < self.pValues[i]:
					gpvalueList[i] = sumProb
				if herfindahlList[x] < self.pValues[i]:
					hvlist[i] = sumProb
				
			for i in range(len(self.critcalValues)):
				if sumProb < self.critcalValues[i]:
					gcritcalValues[i] = gammaList[x]
				elif sumProb >= self.critcalValues[i] and hatcrit[i] == '' and hatcritl[i]== '' and len(herflist)>0:
					hatcrit[i] = numpy.percentile(numpy.array(herflist),97.5) 
					hatcritl[i] = numpy.percentile(numpy.array(herflist),2.5)
					hatcrits[i] = numpy.percentile(numpy.array(herflist),95) 
					hatcritls[i] = numpy.percentile(numpy.array(herflist),5)

				if sumProb < self.critcalValues[i]:
					hcritcalValues[i] = herfindahlList[x]
					
			herflist.append(combindedList[x]['herfindahl'])
					
		self.sGamma['pvalue'] = finalPValue
		self.sGamma['criticalValues'] = gcritcalValues
		self.sGamma['hCritical'] = hatcrit
		self.sGamma['hCriticalLow'] = hatcritl
		self.sGamma['hCriticals'] = hatcrits
		self.sGamma['hCriticalLows'] = hatcritls
		self.sGamma['pValues'] = gpvalueList
		self.sHerfindahl = {}
		self.sHerfindahl['criticalValues'] = hcritcalValues
		self.sHerfindahl['pValues'] = hvlist
		self.sHerfindahl['mean'] = numpy.mean(herfindahlList)
		self.sHerfindahl['std'] = numpy.std(herfindahlList)
		self.sHerfindahl['min'] = numpy.nanmin(herfindahlList)
		self.sHerfindahl['max'] = numpy.nanmax(herfindahlList)
		self.sGValue = {}
		self.sGValue['mean'] = numpy.mean(gValueList)
		self.sGValue['std'] = numpy.std(gValueList)
		self.sGValue['min'] = numpy.nanmin(gValueList)
		self.sGValue['max'] = numpy.nanmax(gValueList)
		
		
		