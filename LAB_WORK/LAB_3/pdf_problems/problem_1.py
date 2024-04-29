import matplotlib.pyplot as plt

# the region of the graphs
x = [4, 4]
y = [0, 10]


# draw the line
plt.plot(x, y, 'brown', label = 'x = 4')
# draw the region
plt.fill_betweenx(y, x[0], color = 'green', alpha =0.5)

# name the level of both axis
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Vertical Constraints: x <= 4 ")

# limit the main graph size
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.legend(loc="upper right")
plt.grid(True)

# display
plt.show()
