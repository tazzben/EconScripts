#!/usr/bin/env python
# encoding: utf-8

from numpy import *
from math import *


testfn_vectorspace = lambda (x): (1-x[0])**2 + 100*(x[1]-x[0]**2)**2

def DownhillSimplex(F, Start, slide=1.0, tol=1.0**-8):
	
	# Setup intial values
	
	n = len(Start)
	f = zeros(n+1)
	x = zeros((n+1,n))
	
	x[0] = Start
	
	# Setup intial X range
	
	for i in range(1,n+1):
		x[i] = Start
		x[i,i-1] = Start[i-1] + slide
	
	# Setup intial functions based on x's just defined
	
	for i in range(n+1):
		f[i] = F(x[i])
	
	# Main Loop operation, loops infinitly until break condition
	counter = 0
	while True:
		
		low = argmin(f)
		high = argmax(f)
		
		# Implement Counter 
		counter+=1
		
		# Compute Migration
		d = (-(n+1)*x[high]+sum(x))/n
		
		if sqrt(dot(d,d)/n)<tol:
			# Break condition, value is darn close
			return (x[low],counter)
			
		newX = x[high] + 2.0*d
		newF = F(newX)
		
		# Bad news, new values is lower than p. low
		
		if newF <= f[low]:
			x[high] = newX
			f[high] = newF
			newX = x[high] + d
			newF = F(newX)
			# Maybe I need to expand
			if newF <= f[low]:
				x[high] = newX
				f[high] = newF
		# Good news, new values is higher
		else:
			# Do I need to contract?
			if newF <= f[high]:
				x[high] = newX
				f[high] = newF
			else:
				# Contraction
				newX = x[high] + 0.5*d
				newF = F(newX)
				if newF <= f[high]:
					x[high] = newX
					f[high] = newF
				else:
					for i in range(len(x)):
						if i!=low:
							x[i] = (x[i]-x[low])
							f[i] = F(x[i])
	
	
# Example Call

(result, counter) =  DownhillSimplex(testfn_vectorspace, array([2.0,2.0]),1.0,1.0e-6)

print "Custom Downhill Simplex:"
print "Final Result: " + str(result)
print "Iteration Count: " + str(counter)


	