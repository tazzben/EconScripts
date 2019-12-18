# EGSimulation - Compute Ellison & Glaeser Critical Regions by Simulation #

By using a simulation of firm sizes (using a lognormal distribution) and specified geographic regions, standard deviations and employee head count, we can compute the critical regions for the Ellison & Glaeser statistic.  In the process, it also calculates Herfindahl values and provides critical regions.

## NOTICE (2019) ##

Modernized versions of this software have been developed at [CasseySmithCV](https://github.com/tazzben/CasseySmithCV) (python module) and [CasseySmithCLI](https://github.com/tazzben/CasseySmithCLI) (command line tool).  These updated versions produce the same results as the older code presented here, but take advantage of changes in the python language and the increased prevalence of multi-core processors. Thus the code executes substantially faster. For new projects, we recommend you use the newer version.   

## Usage ##

You must specify five input files [option switch in brackets]:

* Tranche file: *Cumulative* geographic population file (last value in the file should be 1) - [-t]
* Critical Values: A list of all of the critical values you want to test [-c]
* P Values: A list of the p values you want to test [--pvalues]
* Firm Size: File containing a list of average firm sizes (in terms of employees) [-f]
* Stand Deviations: File containing a list of standard deviations [-s]
* Number of Firms: File containing a list of the number of firms in an industry [-n]
* Destination: File to save output (CSV) [-d]

You must also specify the number of iterations per simulation [-i].  We recommend at least 1000.  If you wish to use the mersenne twister algorithm instead of fortuna for random number generation specify [--twister].  If you wish to not allow non-integer firm head counts, you can specify the option [--roundfirmsize]; or you can change the rounding behavior using [--roundfirmsizedown] or [--roundfirmsizeup].  Specifying [--normal] will create firm size draws from a normal distribution instead of log normal.  Additionally, you can use Françoise Maurel and Béatrice Sédillot (1999)'s specification for both G and gamma [--maurel].

If you wish to censor your results based on Herfindahl values.  You can specify [--HerfCensuredLow] and [--HerfCensuredHigh].  Any simulation that is not in this range will be tossed.  The output file will also contain how many iterations were saved and how many were performed.

### Example Command ###

	./EGSimulation -t "data/tranche.txt" -c "data/criticalvalues.txt" -f "data/size.txt" -s "data/stdev.txt" -n "data/firms.txt" -i 1200 -d "data/output.csv"

## Binary Versions Available ##

If you don't have a copy of Python installed, we've made binary versions of the application available:

1. [Windows](http://storage.googleapis.com/public-downloads/egsimulation_windows.zip)
2. [Mac](http://storage.googleapis.com/public-downloads/egsimulation_mac.zip)

Both versions come pre-bundled with a directory of sample configuration files and an example command.  These applications have been tested on Windows 8.1 and OS X Mavericks, respectively.

## Estimating Sigma ##

When applying this simulation to small geographic regions, it may be possible to access the employee count data for the industry (such as in a city). Under the estimate sigma folder, we have two simple examples of estimating sigma using [R](http://www.r-project.org/) (free) and [Mathematica](http://www.wolfram.com/mathematica/). 

## Simulating Herfindahls ##

In preparation of using our simulator, it might be necessary to simulate Herfindahl values to determine the likely range given a set number of plants in an industry and the sigma value of the underlying normal distribution of plant employment.   For this task, we have two Herfindahl simulators:

1. "Generate Herfindahl Range for Each N and Sigma"
2. "Generate Herfindahl Bins for Each N given a Range of Sigmas"

Like our main application, both simulators take plant size (-f), sigma (-s) and plants (-n) as input text files that the program loops over.  The output file is specified by -d.  The difference between the two simulators is that (1) takes all simulated H values for a given N and sigma and provides a confidence interval (then moves to the next N/sigma combination).  (2) groups all simulated H values for a given N for all specified values of sigma and provided decile bins.

## Notice ##

This code is part of a larger research project published in the *[Journal of Urban Economics](http://doi.org/10.1016/j.jue.2014.02.005)* by Andrew Cassey and Ben Smith (at Washington State University and the University of Nebraska at Omaha, respectfully).  If you want  to use our code to test critical values for your area of interest, feel free.  But, don't be a jerk, give us credit.

|Format|Citation|  
| ------	| ------	|  
|MLA	| Cassey, Andrew J., and Ben O. Smith. "Simulating confidence for the Ellison–Glaeser index." *Journal of Urban Economics* 81 (2014): 85-103.|  
|APA	| Cassey, A. J., & Smith, B. O. (2014). Simulating confidence for the Ellison–Glaeser index. *Journal of Urban Economics*, *81*, 85-103.|  
|Chicago|Cassey, Andrew J., and Ben O. Smith. "Simulating confidence for the Ellison–Glaeser index." *Journal of Urban Economics* 81 (2014): 85-103.|  

BibTeX:

	@article{CasseySmith2014,
	 title={Simulating confidence for the Ellison--Glaeser index},
	 author={Cassey, Andrew J and Smith, Ben O},
	 journal={Journal of Urban Economics},
	 volume={81},
	 pages={85--103},
	 year={2014},
	 publisher={Elsevier}
	 }
