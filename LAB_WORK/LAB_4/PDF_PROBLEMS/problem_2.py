"""
solve the following LP problem using graphical methods
Maximize maximize, z= 8x1 + 10x2 
subject to, 
2x1 + 4x2 <= 100
3x1 + 5x2 <= 120
x1, x2 >= 0

"""

import matplotlib.pyplot as plt
import numpy as np

# calculate the point from the equation
M = (0, 25)
N = (50, 0)
O = (0, 24)
P = (40, 0)

# plot the points
plt.plot(*M, "ro", label = "M(0, 25)")
plt.plot(*N, "go", label = "N(50, 0)")
plt.plot(*O, "bo", label = "O(0, 24)")
plt.plot(*P, "yo", label = "P(40, 0)")

# plot the lines
plt.plot([M[0], N[0]], [M[1], N[1]], label = "2x1 + 4x2 = 100")
plt.plot([O[0], P[0]], [O[1], P[1]], label = "3x1 + 5x2 = 120")

# plot the feasible region according to these lines
x1 = np.linspace(0, 50, 100)
x2_line1 = (100 - 2 * x1) / 4
x2_line2 = (120 - 3 * x1) / 5

# fill the region
plt.fill_between(x1, np.minimum(x2_line1, x2_line2), 0 , where= (x2_line1 >= 0) & (x2_line2 >= 0), color = "gray", alpha = 0.5)


# plot setting
plt.xticks(np.arange(0, 61, step= 5))
plt.yticks(np.arange(0, 61, step= 5))
plt.xlabel("X_1 axis")
plt.ylabel("X_2 axis")
plt.title("Feasible Region for Linear Programming Problem")
plt.grid(True)
plt.legend(loc="upper right")
plt.axis()  # Set aspect ratio to square
plt.show()
