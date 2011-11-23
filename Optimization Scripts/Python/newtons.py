#!/usr/bin/env python
# encoding: utf-8

from numpy import *
from math import *
from numpy.linalg import *

# Function 

testfn_vectorspace = lambda (x): (1-x[0])**2 + 100*(x[1]-x[0]**2)**2

# Derivative

def testfn_d(x):
	return array([2*100*(x[1] - x[0]**2)*(-2*x[0]) - 2*(1.-x[0]), 2*100*(x[1]-x[0]**2)])

# Hessian
	
def hess(x):
	a = zeros((2,2))
	a[0,0] = 2 + 1200*x[0]**2 - 400*x[1]
	a[1,1] = 200
	a[0,1] = -400*x[0]
	a[1,0] = -400*x[0]
	return a



def NewtonsMethod(F,Fprime,Hess,Start,linsearch=False, wolfeval = 1,tol=1.0e-6, epsi=10.0e-8):
	
	def LineSearch(g,x,s,sigma= 10**-1, beta = 10, convergval = 0.00001):
			
		# QFind returns 1 or the proper value (based on the current slope) of the line
		# based on basic rise over run of the distance of the current function with
		# new vs old value
		
		def QFind(alpha):
			if abs(alpha) < convergval:
				return 1
			return (F(x + alpha*s) - F(x))/(alpha * dot(g,s))

		
		alpha = 1.

		# Double alpha until big enough
		while QFind(alpha) >= sigma:
			alpha=alpha * 2

		# BTacking
		while QFind(alpha)< sigma:
			alphap=alpha / ( 2.0* ( 1- QFind(alpha)))
			alpha=max(1.0/beta * alpha, alphap)
		return alpha
	
	# Startup
	g = -dot(inv(Hess(Start)),Fprime(Start))
	xnew = Start+g
	xold = inf
	counter = 0
	while norm(g) > epsi and norm(xold - xnew) > tol:
		# Implement Counter 
		counter+=1
		x = xnew
		# Do Line Search only if set to true
		if linsearch == True:
			alpha = LineSearch(Fprime(x),x,-dot(inv(Hess(x)),Fprime(x)))
		else:
			alpha = wolfeval
		# Set new value for next iteration
		g = -dot(inv(Hess(x)),Fprime(x))
		xnew = x+alpha*g
		xold = x
		
	return (xnew, counter)




# Newtons method 

(result, counter) =  NewtonsMethod(testfn_vectorspace, testfn_d, hess, array([2,2]))

print "Custom Newton:"
print "Final Result: " + str(result)
print "Iteration Count: " + str(counter)


# Newtons method with line search

(result, counter) =  NewtonsMethod(testfn_vectorspace, testfn_d, hess, array([2,2]), True)

print "\n\nCustom Newton with Line Search:"
print "Final Result: " + str(result)
print "Iteration Count: " + str(counter)

# Newtons method with with .1 Wolfe value

(result, counter) =  NewtonsMethod(testfn_vectorspace, testfn_d, hess, array([2,2]), False, 0.1)

print "\n\nCustom Newton with .1 Wolfe value:"
print "Final Result: " + str(result)
print "Iteration Count: " + str(counter)

# Newtons method with with .01 Wolfe value

(result, counter) =  NewtonsMethod(testfn_vectorspace, testfn_d, hess, array([2,2]), False, 0.01)

print "\n\nCustom Newton with .01 Wolfe value:"
print "Final Result: " + str(result)
print "Iteration Count: " + str(counter)