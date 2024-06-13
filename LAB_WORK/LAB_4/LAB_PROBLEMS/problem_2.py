import matplotlib.pyplot as plt
import numpy as np

M = (0, 8.33)
N = (5, 0)
O = (0, 24)
P = (40, 0)

plt.plot(*M, "ro", label = "M(0, 8.33)")
plt.plot(*N, "go", label = "N(5, 0)")
plt.plot(*O, "ro", label = "O(0, 24)")
plt.plot(*P, "go", label = "P(40, 0)")

plt.plot([M[0], N[0]], [M[1], N[1]], "brown", label=" 20x1 + 12x2 = 100")
plt.plot([O[0], P[0]], [O[1], P[1]], "gray",  label="3x1 + 5x2 = 120")

x1 = np.linspace(0, 40, 100)
x2_line1 = (100 - 20 * x1)/ 12
x2_line2 = (120 - 3* x1)/ 5

plt.fill_between(x1, np.minimum(x2_line1, x2_line2), 0, where=(x2_line1 >= 0) & (x2_line2 >= 0), color = "blue", alpha = 0.5)

plt.xticks(np.arange(0, 50, step=10))
plt.yticks(np.arange(0, 35, step=10))
plt.xlabel(" X_1 ")
plt.ylabel(" Y_1 ")
plt.legend()
plt.title("Feasible region of the LPP")
plt.grid(True)
plt.axis()
plt.show()
