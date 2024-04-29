import matplotlib.pyplot as plt


x = [0, 10]
y = [3, 3]
plt.plot(x, y, "red", label="y = 3")
plt.fill_between(x, y[0], color="green", alpha=0.5)
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title(" y <= 3 ")
plt.grid(True)
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.legend(loc="upper right")
plt.show()
