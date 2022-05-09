from scipy.integrate import fixed_quad
from scipy.interpolate import CubicSpline
import numpy as np
#Function in use
def function(x):
     return (x-2)**3 - 3.5*x + 8.0

#derivative
def derivActual(x=4):
    return 3*(x-2)**2 - 3.5
print(derivActual(x=4))
#would need "h" value something is wrong here so I skipped this.
#h = 1E-9
#def CentralDiff(f, h):
    #return ((f+h) - (f-h))/(2*h)
#print(CentralDiff(x=4),h )

#actual integral
def int(a, b):
    upper = (1/4)*(b-2)**4 - (3.5/2)*b**2 + 8.0*b
    lower = (1/4)*(a-2)**4 - (3.5/2)*a**2 + 8.0*a
    return upper-lower
#values could be anything
print(int(0.0, 4.0))

#x = np.linspace(0.0, 4.0, 5)
#y = function(x)

x= np.array([0,1,2,3,4])
y = np.array([2,-1.5,1,3.5,0])
cs = CubicSpline(x, y)

result, CubSp = fixed_quad(cs, 0.0, 4.0, n=2)
print(result)

result, func = fixed_quad(function, 0.0, 4.0, n=2)
print(result)
#function prints and spline prints



print(function(0))
print(cs(0,2))




print(function(2))
print(cs(2,1))


print(function(3))
print(cs(3,3.5))

print(function(4))
print(cs(4,0))