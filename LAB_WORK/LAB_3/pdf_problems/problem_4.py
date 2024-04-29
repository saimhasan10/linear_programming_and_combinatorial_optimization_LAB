import matplotlib.pyplot as plt
import numpy as np

# x values
x = np.linspace(0, 10, 100)
# print(x)

# y values
y = (-3/4) * x + 6
# print(y)

# draw lines
plt.plot(x, y, "magenta", label="(1/2)x + (2/3)y = 4")

# fill the region
plt.fill_between(x, y, 0, where = ((1/2) * x + (2/3) * y) <= 4,  color="lime", alpha=0.5)

plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Constraints Involving Fractions:  where (1/2)x + (2/3)y <= 4")


plt.xlim(0, 10)
plt.ylim(0, 10)
plt.legend(loc="upper right")

plt.grid(True)
# show the graph
plt.show()
