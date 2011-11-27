# EGSimulation - Compute Ellison & Glaeser Critical Regions by Simulation #

By using a simulation of firm sizes (using a lognormal distribution) and specified geographic regions, standard deviations and employee head count, we can compute the critical regions for the Ellison & Glaeser statistic.  

## Usage ##

You must specify five input files [option switch in brackets]:

* Tranche file: *Commutative* geographic population file (last value in the file should be 1) - [-t]
* Critical Values: A list of all of the critical values you want to test [-c]
* Firm Size: File containing a list of average firm sizes (in terms of employees) [-f]
* Stand Deviations: File containing a list of standard deviations [-s]
* Number of Firms: File containing a list of the number of firms in an industry [-n]
* Destination: File to save output (CSV) [-d]

You must also specify the number of iterations per simulation [-i].  We recommend at least 1000.  If you wish to use the mersenne twister algorithm instead of fortuna for random number generation specify [--twister].  If you wish to allow non-integer firm head counts, you can specify the option [--nonintfirmsize].  Specifying [--normal] will create firm size draws from a normal distribution instead of log normal.

### Example Command ###

	./EGSimulation -t "data/tranche.txt" -c "data/criticalvalues.txt" -f "data/size.txt" -s "data/stdev.txt" -n "data/firms.txt" -i 1200 -d "data/output.csv"

## Notice ##

This is area of current research by Andrew Cassey and Ben Smith (both at Washington State University - a paper will be forthcoming).  If you want  to use our code to test critical values for your area of interest, feel free.  But, don't be a jerk, give us credit.