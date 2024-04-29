import matplotlib.pyplot as plt

# the region we show
x = [0, 10]
y = [3, 3]

# draw the line
plt.plot(x, y, 'red', label = 'y = 3')
plt.fill_between(x, y[0], color = 'gray', alpha = 0.5)

# name the level of both axis
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title(" Horizontal Constraints:  y <= 3 ")

# limit the main graph size
plt.grid(True)
plt.xlim(0, 10)
plt.ylim(0, 8)
plt.legend(loc='upper right')

# display
plt.show()
