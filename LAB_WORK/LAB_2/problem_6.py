# 6. Draw a straight line.

import matplotlib.pyplot as plt

# define the coordinates of the line
x = [1, 2, 3, 4, 5]
y = [10, 8, 6, 4, 2]

# plot the line
plt.plot(x,y)

# add the level and title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Straight line ")

# display it
plt.show()
