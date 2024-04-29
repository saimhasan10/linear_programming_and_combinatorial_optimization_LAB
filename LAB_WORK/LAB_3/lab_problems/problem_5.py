import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = (3 * x) / 4
plt.plot(x, y, "red", label="3x - 4y = 0")
plt.fill_between(x, y, 10, where=(x * 3 / 4 <= y), color="green", alpha=0.5)
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("3x - 4y <= 0")
plt.xlim(0, 5)
plt.ylim(0, 5)
plt.legend(loc="upper left")
plt.grid(True)
plt.show()
