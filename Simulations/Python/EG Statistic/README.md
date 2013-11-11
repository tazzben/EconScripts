# EGSimulation - Compute Ellison & Glaeser Critical Regions by Simulation #

By using a simulation of firm sizes (using a lognormal distribution) and specified geographic regions, standard deviations and employee head count, we can compute the critical regions for the Ellison & Glaeser statistic.  In the process, it also calculates Herfindahl values and provides critical regions.

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


## The Super Easy Way to Install (Macports) ##

You can install this application using MacPorts!  Type the following:

<pre>
sudo port -v selfupdate
sudo port install EGSimulation
</pre>

This method takes care of all dependancies and can manage updates for you.  For information on installing MacPorts, please visit [their site](http://www.macports.org/install.php).

## Estimating Sigma ##

When applying this simulation to small geographic regions, it may be possible to access the employee count data for the industry (such as in a city). Under the estimate sigma folder, we have two simple examples of estimating sigma using [R](http://www.r-project.org/) (free) and [Mathematica](http://www.wolfram.com/mathematica/). 


## Notice ##

This is area of current research by Andrew Cassey and Ben Smith (both at Washington State University - a paper has been submitted to JUE -- [working paper available here](http://bensresearch.com/downloads/EGstat.pdf)).  If you want  to use our code to test critical values for your area of interest, feel free.  But, don't be a jerk, give us credit.