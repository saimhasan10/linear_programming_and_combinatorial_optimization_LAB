import matplotlib.pyplot as plt
import numpy as np

# x values
x = np.linspace(0, 10, 100)

# y values
y = (3 * x )/4

# draw the line
plt.plot(x, y, "brown", label="3x - 4y = 0")

# fill the region
plt.fill_between(x, y, 10, where=( x * 3 / 4 <= y ), color ="lightblue", alpha = 0.5 )


plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Constraints with Negative Coefficients: where 3x - 4y <= 0")


plt.xlim(0, 5)
plt.ylim(0, 5)
plt.legend(loc="upper left")

plt.grid(True)
# show the graph
plt.show()
