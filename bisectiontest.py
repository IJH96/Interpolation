import numpy as np
import matplotlib as plt



def find_sign_change(f,step,a,b):
    x=a
    pairs = []
    while (x < b):
        if (f(x+step)/f(x)<0):
            pairs.append([x,x+step])
            print(pairs)

        x+=step
    return pairs


def bisect(f,pairs, tolerance):
    zeros = []
    for pair in pairs:
        midP =(pair[1] +pair[0])/2.0
        while abs(f(midP)) > tolerance:
            if (f(midP)/f(pair[0]) < 0):
                 pair[1] = midP
            else: 
                pair[0] = midP
            midP = (pair[1] +pair[0])/2.0
        zeros.append(midP)
                
                
    return zeros
def f(x):
     if (x==0):
         return 1.0
     else: 

        return np.sin(x)/x
    
pairs = find_sign_change(f, 0.25, 0.0, 10.0)
zeros = bisect(f,pairs, 1E-8)

print(zeros)