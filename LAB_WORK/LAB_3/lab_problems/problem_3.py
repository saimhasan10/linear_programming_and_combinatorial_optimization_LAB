import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 400)
y = (20 - 4 * x) / 5
plt.plot(x, y, "red", label="4x + 5y = 20")
plt.fill_between(x, y, 0,  color="green", alpha=0.5)
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Constraints & Inequalities: 4x + 5y <= 20")
plt.xlim(0, 5)
plt.ylim(0, 5)
plt.legend(loc="upper right")
plt.grid(True)
plt.show()
