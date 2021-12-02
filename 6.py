import math
from math import sin
from math import cos
from math import fabs
from scipy import optimize

x =-0.1
y =-0.8

def itter_met(y):
    return 0.8-cos(y+0.5)
def itter_met2(x):
    return -4/5+sin(x)/2
    
def it_method(x,y,e):
        xn = x
        yn = y
        xn1 = itter_met2(x)
        yn1 = itter_met(y)
        n = 1
        
        while((fabs(xn1 - xn) >= e) and (fabs(yn1 - yn) >= e)):
            xn = xn1
            yn = yn1
            xn1 = itter_met2(yn)
            yn1 = itter_met(xn1)
            n += 1
            
        print("x1 = ", xn, "y1 =", yn, "Itteration = ", n)
        
it_method(x, y, 0.001)
def f(x):
    return cos(x[1]+0.5) + x[0] - 0.8, sin(x[0]) -2*x[1] - 1.6
s = optimize.root(f, [0,0],method= 'hybr')
print (s.x)
