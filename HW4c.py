#region imports
import numpy as np
from scipy.linalg import solve
#endregion

def matrixsolve(A_aug):
    '''function creates augmented matrix and populates with samples from problem c'''
    A = A_aug[:, :-1]
    b = A_aug[:, -1]
    return solve(A, b)

Aaug1 = np.array([          #1st matrix
    [3, 1, -1, 2],
    [1, 4, 1, 12],
    [2, 1, 2, 10]
])

Aaug2 = np.array([          #2nd matrix
    [3, 1, 4, 12, 12],      #matrix reorganized
    [1, -10, 2, 4, 2],
    [-1, 2, 7, 3, 37],
    [9, 2, 3, 4, 21]
])


print("Problem 1:")                 #problem 1 print statements
for i, sol in enumerate(matrixsolve(Aaug1)):
    print(f"x{i+1} =", sol)


print("\nProblem 2:")               #problem 2 print statements
for i, sol in enumerate(matrixsolve(Aaug2)):
    print(f"x{i+1} =", sol)