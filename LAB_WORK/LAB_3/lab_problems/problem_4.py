import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 400)
y = (2.5 - 0.5 * x) / 0.25
plt.plot(x, y, "red", label="0.5x + 0.25y = 2.5")
plt.fill_between(x, y, 0, color="green", alpha=0.5, where=(y >= 0))
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title(" 0.5x + 0.25y <= 2.5")
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.legend(loc="upper right")
plt.grid(True)
plt.show()
