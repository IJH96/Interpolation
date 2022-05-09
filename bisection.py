import numpy as np
def find_sign_changes(f, step, a, b):
    pairs = []
    x = a
    while (x < b):
        if (f(x + step)/f(x) < 0):
            pairs.append([x,x+step])
        x += step
    return pairs
def bisect(f, pairs, tolerance):
    zeros = []
    for pair in pairs:
        midpoint = (pair[1] - pair[0])/2.0 + pair[0]
        while (abs(f(midpoint)) > tolerance):
            if (f(midpoint)/f(pair[0]) < 0): pair[1] = midpoint
            else: pair[0] = midpoint
            midpoint = (pair[1] - pair[0])/2.0 + pair[0]
        zeros.append(midpoint)
    return zeros