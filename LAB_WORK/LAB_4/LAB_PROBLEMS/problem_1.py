import matplotlib.pyplot as plt
import numpy as np

M = (0, 6)
N = (5, 0)
O = (0, 20)
P = (20, 0)

plt.plot(*M, "yo", label = "M(0, 6)")
plt.plot(*N, "bo", label = "N(5, 0)")
plt.plot(*O, "yo", label = "O(0, 20)")
plt.plot(*P, "bo", label = "P(20, 0)")

plt.plot([M[0], N[0]], [M[1], N[1]], 'brown', label = "12x1 + 10x2 = 60")
plt.plot([O[0], P[0]], [O[1], P[1]], 'gray', label = "4x1 + 4x2 = 80")

x1 = np.linspace(0, 20, 100)
x2_line1 = (60 - 12 * x1) / 10
x2_line2 = (80 - 4 * x1) / 4

plt.fill_between(x1, np.minimum(x2_line1, x2_line2), 0, where=(x2_line1 >= 0) & (x2_line2 >= 0), color = "blue", alpha = 0.5)

plt.xticks(np.arange(0, 30, step = 5))
plt.yticks(np.arange(0, 30, step = 5))
plt.xlabel(" X_1 ")
plt.ylabel(" Y_1 ")
plt.legend()
plt.title("Feasible region of the LPP")
plt.grid(True)
plt.axis()
plt.show()

