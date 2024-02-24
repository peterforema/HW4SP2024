#region imports
import numpy as np
from scipy.optimize import fsolve
#endregion

def equation1(x):
    '''equation from homework 4'''
    return x - 3 * np.cos(x)

def equation2(x):
    '''''equation from homework 4'''
    return np.cos(2*x) * x**3

# Find roots of equation 1
roots1 = fsolve(equation1, x0=[0, 2, 4])
print("Roots of equation 1:", roots1)

# Find roots of equation 2
roots2 = fsolve(equation2, x0=[0, 2, 4])
print("Roots of equation 2:", roots2)

# Check if functions intersect
intersections = fsolve(lambda x: equation1(x) - equation2(x), x0=[0, 2, 4])     #if else statement from CHAT
if len(intersections) > 0:
    print("Functions intersect at x =", intersections)
else:
    print("Functions do not intersect.")
