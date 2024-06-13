import matplotlib.pyplot as plt
import numpy as np

M = (0, 8)
N = (2, 0)
O = (0, 15)
P = (9, 0)
Q = (0, 9)
R = (10, 0)

plt.plot(*M, "mo", label="M(0, 8)")
plt.plot(*N, "go", label="N(2, 0)")
plt.plot(*O, "bo", label="O(0, 15)")
plt.plot(*P, "co", label="P(9, 0)")
plt.plot(*Q, "yo", label="Q(0, 9)")
plt.plot(*R, "ro", label="R(10, 0)")

plt.plot([M[0], N[0]], [M[1], N[1]], "brown", label="8x + 2y = 16")
plt.plot([O[0], P[0]], [O[1], P[1]], "green", label="5x + 3y = 45")
plt.plot([Q[0], R[0]], [Q[1], R[1]], "gray", label="9x + 10y = 90")

x = np.linspace(0, 10, 400)

y1 = (16 - 8 * x) / 2
y2 = (45 - 5 * x) / 3
y3 = (90 - 9 * x) / 10

plt.fill_between(
    x,
    np.maximum(y1, 0),
    np.minimum(np.minimum(y2, y3), 10),
    where=(y1 <= y2) & (y1 <= y3) & (y2 >= 0) & (y3 >= 0),
    color="lightblue",
    alpha=0.5,
)

# plt.xlim(0, 10)
# plt.ylim(0, 10)
plt.xticks(np.arange(0, 15, step=1))
plt.yticks(np.arange(0, 20, step=1))
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.legend()
plt.title("Showing feasible region for LPP")
plt.grid(True)
plt.show()
