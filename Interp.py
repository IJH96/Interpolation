import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.interpolate import CubicSpline
def langrange_interpolation(x, x_i, y_i):
    N = len(x_i)
    result = 0
    for i in range(0,N):
        product =1 
        for j in range(0,N):
            if (j!=i):
                product *=(x - x_i[j])/(x_i[i] - x_i[j])
        result +=product*y_i[i]
    return result

x_i = np.array([0,3,5,7,13])
y_i = np.array([-7,6,-1,11,18])
cs = CubicSpline(x_i, y_i)
print("y(2)= ",langrange_interpolation(2, x_i, y_i) )
print("y(9)= ",langrange_interpolation(9, x_i, y_i) )
print("y(2)= ",cs(2.0))
print("y(2)= ",cs(9.0))
def gaussian(x,mu,sigma):
    return np.exp((-(x-mu)**2)/(2*sigma**2))*math.sqrt(1/(2*math.pi*sigma))

x = np.linspace(-4,4,10)
y = gaussian(x, 0.0, 1.0)
cs_g = CubicSpline(x,y)
x_g = np.linspace(-4,4,1000)
y_g = gaussian(x_g, 0.0, 1.0)

y_1 = langrange_interpolation(x_g, x, y)
y_cs = cs_g(x_g)


plt.plot(x_g,y_g)
plt.plot(x_g,y_1)
plt.plot(x_g,y_cs)
plt.plot(x,y,",")
plt.show()

#These lines don't line up on the edges after looking at the graph. 
#The reason this happens is because bisection takes points on either side of the value. 
#So at the extreme positions on the edges there are no values to fit the graph, hence the differences.

#I probably will trust the cubic spline version more as it is better fitted. 
#Also, the spline method seems more complex and uses continuity from differentiation.