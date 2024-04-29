import matplotlib.pyplot as plt


x = [5, 5]
y = [0, 10]
plt.plot(x, y, "red", label="x = 5")
plt.fill_betweenx(y, 5, 20, color="green", alpha=0.5)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title(" x >= 5 ")
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.legend(loc="upper right")
plt.grid(True)
plt.show()
