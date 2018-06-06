#method 1: analytical solution
import numpy as np
def f(x):
    return (x**3)/3-np.exp(-x)+10*np.log(x)
print (f(10)-f(1), 'the analytical solution')


#method 2: Trapezoidal rule
def f1(x):
    return (x**2+np.exp(-x)+10/x)

#def trap(N):
    N=100.
    dx=(10-1)/(N-1.)
    #print ("The width of the trapezoid is "), dx
    sum=0
    x=1.
    while x<10:
        sum=sum+2*f1(x)
        #print sum
        #print x
        x=x+dx
    sum=sum+ f1(x)
    
print ("Integral by trapezoid method is", dx*sum*0.5)
import matplotlib.pyplot as plt

#method 3: Using scipy
import scipy as sp
from scipy.integrate import quad
a,error=scipy.integrate.quad(f1,1,10)
print("Integral using scipy is")
print(a)
print(error)

""" We get different results from trapezoid method and integtrate.quad due to the number of iterations performed and the termination criteria"""

mat

