import numpy as np
from scipy.optimize import curve_fit
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
import bisection
# Make the font a nice serif font instead of sans serif
# which looks weird as a math font.

#Sadly this did not work as Nimbus Roman was not found for me.

#plt.rcParams["font.family"] = "Nimbus Roman"
#plt.rcParams['mathtext.fontset'] = 'custom'
#plt.rcParams['mathtext.rm'] = 'Nimbus Roman'
#plt.rcParams['mathtext.it'] = 'Nimbus Roman:italic'
#plt.rcParams['mathtext.bf'] = 'Nimbus Roman:bold'
#plt.rcParams['mathtext.cal'] = 'Nimbus Roman'
# Simply harmonic oscillator model. The d parameter is to adjust
# the vertical offset due to manual placement of the axes.
def simple_harmonic_oscillator(x, A, omega, phi, d):
    return A*np.cos(omega*x + phi) + d
# Read in the data from the file
t, y = np.loadtxt("SHM-200g.txt", unpack=True)
# Generate some uncertainties
sig = np.full(len(y), 0.001)
# Amplitude estimate
A = (y.max() - y.min())/2.0
# Get estimate of period by finding zeros, averaging distance
# between zeros, then multiplying by 2
cs = CubicSpline(t, y)
pairs = bisection.find_sign_changes(cs, 0.1, t.min(), t.max())
zeros = bisection.bisect(cs, pairs, 1E-10)
T = 0
for i in range(1,len(zeros)):
    T += zeros[i] - zeros[i-1]
T = 2.0*T/(len(zeros)-1)
# Get angular frequency from period
omega = 2.0*np.pi/T
# Get the phase angle from the value at "zero"
phi = np.arccos(y[0]/A)
# Set some value for d
d = 0.0
# Put initial parameter guesses into list
theta_0 = [A, omega, phi, d]
# Call the curve_fit function to get best fitting parameters
# and covariance
theta, cov = curve_fit(simple_harmonic_oscillator, t, y, p0=theta_0, sigma=sig)
# Print best fitting parameters and uncertainties
names = ['A', 'omega', 'phi', 'd']
for i in range(0,len(theta)):
    print('{0:>5}'.format(names[i]), '=', '{0:>21}'.format(theta[i]), '+/-', '{0:<21}'.format(np.sqrt(cov[i][i])))
# Get correlation matrix
cor = np.zeros_like(cov)
for i in range(0,len(theta)):
    for j in range(0,len(theta)):
        cor[i][j] = cov[i][j]/np.sqrt(cov[i][i]*cov[j][j])
print(cor)
# Create a graph of the best fitting function and the data points
t_m = np.linspace(t.min(), t.max(), 1000) 
# generate a bunch of points to evaluate model function at
y_m = simple_harmonic_oscillator(t_m, theta[0], theta[1], theta[2], theta[3]) 
# get model function w/ best fitting parameters
# Label the axes. The $ signs signify math text
plt.xlabel('$t$ (s)') 
plt.ylabel('$y$ (m)')

# Plot the data and save the plot to a file
plt.plot(t_m, y_m)

plt.errorbar(t,y,sig, fmt=".")
plt.show()
plt.savefig('shmPlot.pdf',bbox_inches='tight')

#The middle values are anti correlated strongly. Not sure why? 
#I know that the correlation and the two standard deviations matter though so one of those changed.
#Also, they have the greater relative standard deviation value of roughly 0.93.
#The edges have a very low correllation value of 1.12
#The standard deviation should be higher if the covariance is higher.