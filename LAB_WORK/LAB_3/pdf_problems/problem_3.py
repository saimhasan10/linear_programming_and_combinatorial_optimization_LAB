import matplotlib.pyplot as plt
import numpy as np

# x values
x = np.linspace(0, 5, 100)

#  y values according to the equation 5x + 4y <= 20
y = (-5/4) * x +5
# print(y)

plt.plot(x, y, 'teal', label="5x + 4y = 20")

# fill the region
plt.fill_between(x, y, 0, where=(5 * x + 4 * y) <= 20, color="orange", alpha=0.5)

# name both axis
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Constraints & Inequalities: 5x + 4y <= 20")


plt.xlim(0, 10)
plt.ylim(0, 10)
plt.legend(loc="upper right")
plt.grid(True)
# show the graph
plt.show()
