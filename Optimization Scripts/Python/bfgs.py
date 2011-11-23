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


def Newton_BFGS(F,Fprime, Start, epsi = 10e-8, tol = 10e-6, sigma= 10**-1, beta = 10 ):
	
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
	x = Start
	xold = inf
	N = shape(x)[0]
	H = 1.0 * eye(N)
	counter = 1
	alpha = 1
	g = Fprime(x)
	while norm(g) > epsi and norm(xold - x) > tol:
		s = -dot(H,g)
		# Repeating the linesearch
		alpha = LineSearch(g,x,s)
		x = x+alpha*s
		gold = g
		g = Fprime(x)
		y = (g - gold)/alpha
		dotsy = dot(s,y)
		if dotsy>0:
			# Update H using estimation technique
			z = dot(H,y)
			H += outer(s,s)*(dot(s,y) + dot(y, z))/dotsy**2 - (outer(z,s)+ outer(s, z))/dotsy
		# Implement Counter 
		counter+=1

	return (x , counter)

(result, counter) =  Newton_BFGS(testfn_vectorspace, testfn_d, array([2,2]))

print "Custom BFGS:"
print "Final Result: " + str(result)
print "Iteration Count: " + str(counter)