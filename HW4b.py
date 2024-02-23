from scipy.optimize import fsolve
import numpy as np

def equations(x):
    eq1 = x[0] - 3 * np.cos(x[0])
    eq2 = np.cos(2*x[0]) * (x[0]**3) - 3
    return [eq1, eq2]


initial_guess = [0, 1]                      #guess is for the roots of the equations
roots = fsolve(equations, initial_guess)       # Solve the equations

print("Roots of the equations:")
print("x - 3*cos(x) = 0:", roots[0])
print("cos(2x)*(x^3) = 3:", roots[1])
