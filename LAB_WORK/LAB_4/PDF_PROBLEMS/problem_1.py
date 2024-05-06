"""
solve the following LP problem using graphical methods
Maximize maximize, z = 6x1 + 8x2 
subject to, 
5x_1 + 10x_2 <= 60
4x_1 + 4x_2 <= 40
x1, x2 >= 0

"""

import matplotlib.pyplot as plt
import numpy as np


# calculate the points from the equations
M = (12, 0)
N = (0, 6)
O = (0, 10)
P = (10, 0)


#  plot the lines
plt.plot(*M, 'ro', label = "M(12, 0)")
plt.plot(*N, 'bo', label = "N(0, 6)")
plt.plot(*O, 'go', label = "O(0, 10)")
plt.plot(*P, 'yo', label = "P(10, 0)")

# draw the lines
plt.plot([M[0], N[0]], [M[1], N[1]], label="5x_1 + 10x_2 = 60")
plt.plot([O[0], P[0]], [O[1], P[1]], label="4x_1 + 4x_2 = 40")


# plot the feasible region according to these lines
x1 = np.linspace(0, 12, 100)
x2_line1 = (60 - 5 * x1) / 10
x2_line2 = (40 - 4*x1)/ 4

#  fill the region
plt.fill_between(x1, np.minimum(x2_line1, x2_line2), 0, where=(x2_line1 >= 0) & (x2_line2 >= 0), color ='gray', alpha = 0.5)

# graph setting
plt.xticks(np.arange(0, 16, step = 1))
plt.yticks(np.arange(0, 16, step = 1))
plt.xlabel("X_1 axis")
plt.ylabel("X_2 axis")
plt.title("Feasible Region for Linear Programming Problem")
plt.grid(True)
plt.legend(loc = "upper right")
plt.axis()  # Set aspect ratio to square
plt.show()
