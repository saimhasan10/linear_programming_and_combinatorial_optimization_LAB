import matplotlib.pyplot as plt
import numpy as np

# x values
x = np.linspace(-10, 10, 100)
# print(x)

# y values
y = (3 + 2 * x) / 3

# handle the non-negative values for shading
y_shade = np.maximum(0, (3 + 2 * x) / 3)

# plot the line
plt.plot(x, y, "gray", label = "-2x + 3y = 3")

# fill the region
plt.fill_between(x, 0, y_shade, color="green", alpha=0.5)


plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Constraints with Negative Coefficients: where -2x + 3y <= 3")


plt.xlim(0, 10)
plt.ylim(0, 10)
plt.legend(loc="upper left")

plt.grid(True)
# show the graph
plt.show()
