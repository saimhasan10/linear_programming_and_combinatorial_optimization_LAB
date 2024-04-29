import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 100)

y= 6 - 2 * x 

plt.plot(x, y, 'brown', label = "2x + y = 6")

plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Equality Constraints:  where 2x + y = 6")


plt.xlim(0, 8)
plt.ylim(0, 10)
plt.legend(loc="upper right")

plt.grid(True)
# show the graph
plt.show()
