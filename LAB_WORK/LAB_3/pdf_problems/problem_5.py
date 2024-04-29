import matplotlib.pyplot as plt
import numpy as np 

# x values
x  = np.linspace(0, 10, 100)
# print(x)

# y values
y = (2.5 - 0.5 * x) / 0.25
# print(y)

# plot the line
plt.plot(x, y, "brown", label="0.5x + 0.25y = 2.5")

# fill the region
plt.fill_between(x, y, 0, where=(0.5 * x + 0.25 * y) <= 2.5, color="purple", alpha=0.5)


plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Constraints with Decimal Points:  where 0.5x + 0.25y <= 2.5")


plt.xlim(0, 8)
plt.ylim(0, 10)
plt.legend(loc="upper right")

plt.grid(True)
# show the graph
plt.show()
