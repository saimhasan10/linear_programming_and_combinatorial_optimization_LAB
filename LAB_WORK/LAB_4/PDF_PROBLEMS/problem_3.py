"""
solve the following LP problem using graphical methods
Maximize maximize, z=  2x + 5y
subject to, 
x + 2y = 16
5x + 3y =45
x1, x2 >= 0

"""

import matplotlib.pyplot as plt
import numpy as np

# # calculate the point from the equation
M = (0, 8)
N = (16, 0)
O = (0, 15)
P = (9, 0)

# plot the points
plt.plot(*M, "ro", label = "M(0,8)")
plt.plot(*N, "bo", label = "N(16, 0)")
plt.plot(*O, "go", label = "O(0, 15)")
plt.plot(*P, "yo", label = "P(9,0)")

# Draw lines
plt.plot([M[0], N[0]], [M[1], N[1]], label="x + 2y = 16")
plt.plot([O[0], P[0]], [O[1], P[1]], label="5x + 3y = 45")

# Plot feasible region
x1 = np.linspace(0, 10, 100)
x2_line1 = (16 - x1) / 2
x2_line2 = (45 - 5*x1) / 3
plt.fill_between(x1, np.minimum(x2_line1, x2_line2), 0, where=(x2_line1 >= 0) & (x2_line2 >= 0), color='gray', alpha=0.5)

# Plot settings
plt.xticks(np.arange(0, 21, step=1))
plt.yticks(np.arange(0, 21, step=1))
plt.xlabel("x")
plt.ylabel("y")
plt.title("Feasible Region for Linear Programming Problem")
plt.grid(True)
plt.legend()

# Set aspect ratio to square
plt.axis()
plt.show()
