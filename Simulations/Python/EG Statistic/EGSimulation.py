#!/usr/bin/env python
import optparse
import os
import platform
import sys
import codecs
from gammaSimulation import *
import csv
from decimal import *

def isNumeric(value):
	return str(value).replace('.','').strip().isdigit()

def fileExists(value):
    if os.path.isfile(os.path.expanduser(value.strip())):
        return os.path.abspath(os.path.expanduser(value.strip()))
    else:
        print "I can't find the file" + value
        sys.exit()

def isReturnFile(myfile):
	if os.path.abspath(os.path.expanduser(myfile.strip())) != False:
		return os.path.abspath(os.path.expanduser(myfile.strip()))
	else:
		print 'You can\'t save to that location'
		sys.exit()

def WriteFile(filename,criticalvalues,data):
	fieldList = ['NumberOfFirms','FirmSize','StDev','GammaMean','GammaMin','GammaMax','GammaStd','HerfindahlMean','HerfindahlMin','HerfindahlMax','HerfindahlStd','GValueMean','GValueMin','GValueMax','GValueStd','PValue']
	
	for x in range(len(criticalvalues)):
		fieldList.append("C" + str(criticalvalues[x]).replace('.','').strip())
	
	if os.path.isfile(filename) == False:
		mf = open(filename, 'wb')
		myfile = csv.writer(mf)
		myfile.writerow(fieldList)
		mf.close()
	
	myfile = open(filename,'ab+')
	WriteFile = csv.DictWriter(myfile,fieldList)
	WriteFile.writerow(data)
	myfile.close()
	print "Saving # of Firms: " + str(data['NumberOfFirms']) + ", Firm Size: " + str(data['FirmSize']) + ", StDev: " + str(data['StDev'])


def RunSimulation(numberoffirmsList,firmsizeList,sdevList,trancheList,criticalvaluesList,loopsc,destination, twister):
	for x in range(len(numberoffirmsList)):
		for y in range(len(firmsizeList)):
			for z in range(len(sdevList)):
				resultDic = {}
				cGS = gammaSimulation(firmsizeList[y], sdevList[z], int(numberoffirmsList[x]), trancheList, criticalvaluesList, loopsc, twister)
				gamma = cGS.getGamma()
				herfindahl = cGS.getHerfindahl()
				gValue = cGS.getGValue()
				del cGS
				resultDic['NumberOfFirms'] = numberoffirmsList[x]
				resultDic['FirmSize'] = firmsizeList[y]
				resultDic['StDev'] = sdevList[z]
				
				resultDic['GammaMean'] = gamma['mean']
				resultDic['GammaMin'] = gamma['min']
				resultDic['GammaMax'] = gamma['max']
				resultDic['GammaStd'] = gamma['std']
				
				
				resultDic['HerfindahlMean'] = herfindahl['mean']
				resultDic['HerfindahlMin'] = herfindahl['min']
				resultDic['HerfindahlMax'] = herfindahl['max']
				resultDic['HerfindahlStd'] = herfindahl['std']
				
				resultDic['GValueMean'] = gValue['mean']
				resultDic['GValueMin'] = gValue['min']
				resultDic['GValueMax'] = gValue['max']
				resultDic['GValueStd'] = gValue['std']
				
				resultDic['PValue'] = gamma['pvalue']
				
				
				
				lcv = gamma['criticalValues']
				
				for cv in range(len(criticalvaluesList)):
					key = "C" + str(criticalvaluesList[cv]).replace('.','').strip()
					resultDic[key] = lcv[cv]
				WriteFile(destination,criticalvaluesList,resultDic)
				
 
def loadFile(value):
	empty_data = []
	with open(value.strip(), 'rU') as f:
		read_data = f.readlines()
	
	for x in range(len(read_data)):
		if isNumeric(read_data[x].strip()):
			empty_data.append(float(read_data[x].strip()))
			
	return empty_data

def main():
	desc = 'Tool to simulate EG statistic'
	p = optparse.OptionParser(description=desc)
	p.add_option('--tranchefile', '-t', dest="tranche", help="File containing geographic tranches", default='', metavar='"<File Path>"')
	p.add_option('--criticalvalues', '-c', dest="criticalvalues", help="File containing critical values to test", default='', metavar='"<File Path>"')
	p.add_option('--firmsize', '-f', dest="firmsize", help="File containing firm size (head count)", default='', metavar='"<File Path>"')
	p.add_option('--sdev', '-s', dest="sdev", help="File containing the standard deviations to test", default='', metavar='"<File Path>"')
	p.add_option('--numberoffirms', '-n', dest="numberoffirms", help="File containing the number of firms (in an industry) to test", default='', metavar='"<File Path>"')
	p.add_option('--iterations', '-i', dest="iterations", help="Number of iterations to run for each simulation", default='5', metavar='"<Integer Value>"')
	p.add_option('--destination', '-d', dest="destination", help="Main csv file to save simulation(s) output", default='', metavar='"<File Path>"')
	p.add_option("--twister", action="store_true", dest="twister", default=False, help="Use mersenne twister for random number generation instead of fortuna")
	
	(options, arguments) = p.parse_args();
	
	if isNumeric(options.iterations):
		loopcount = int(options.iterations)
		if loopcount<1:
			print 'Your simulation must run for at least one loop'
			sys.exit()
	else:
		print 'You must specify a number for iterations'
		sys.exit()
	
	if len(options.destination)>0:
		destination = isReturnFile(options.destination.strip())
	
	if len(options.tranche)>0 and len(options.criticalvalues)>0 and len(options.firmsize)>0 and len(options.numberoffirms)>0 and len(options.sdev)>0:
		tranchefile = fileExists(options.tranche)
		criticalvaluesfile = fileExists(options.criticalvalues)
		firmsizefile = fileExists(options.firmsize)
		numberoffirmsfile = fileExists(options.numberoffirms)
		sdevfile = fileExists(options.sdev)
		
		trancheList = loadFile(tranchefile)
		criticalvaluesList = loadFile(criticalvaluesfile)
		firmsizeList = loadFile(firmsizefile)
		numberoffirmsList = loadFile(numberoffirmsfile)
		sdevList = loadFile(sdevfile)
		
		RunSimulation(numberoffirmsList,firmsizeList,sdevList,trancheList,criticalvaluesList,loopcount,destination,options.twister)
		
	else:
		print 'You must specify files for tranche, critical values, firm size, number of firms, standard deviation'
		sys.exit()	

if __name__ == '__main__':
    main()