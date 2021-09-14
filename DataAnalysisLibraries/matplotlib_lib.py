import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import numpy as np

# https://matplotlib.org/

data = [ 3, 2, 1, 0, 1, 2, 3 ]
rand1 = np.random.rand(50)
rand2 = np.random.rand(50)
pts = np.random.rand(50, 2)
pts2 = np.random.rand(50, 2)

# # basic plot
# plt.plot(data)
# plt.show()

# # two data sets
# plt.plot(rand1)
# plt.plot(rand2, color="red")
# plt.show()

# # scatter
# plt.scatter(rand1, rand2)
# plt.show()

# 2D data set
# plt.scatter(pts[:, 0], pts[:, 1]))
# plt.show()

# settings - marker shape, size, color, legend, axis labels, scale, ...
# axis formatting, figure size, margins - need to be done in advance
# fig, ax = plt.subplots(figsize=(6,3))
fig, ax = plt.subplots()
ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
# plt.subplots_adjust(left=0.2, bottom=0.2, right=0.8, top=0.9, wspace=0, hspace=0)

# https://matplotlib.org/api/
# https://matplotlib.org/api/markers_api.html
plt.scatter(pts[:, 0], pts[:, 1], s=30, c='red', marker='s', label="red data")
plt.scatter(pts2[:, 0], pts2[:, 1], s=20, c='g', marker='P', label="green data") # '#0f0f0f', (0.1, 0.2, 0.3)

# https://matplotlib.org/tutorials/intermediate/legend_guide.html
plt.legend(loc='upper right') # center, right, left, upper, lower, best

# axis settings
# https://matplotlib.org/api/axes_api.html
plt.xlabel('Width')
plt.ylabel('Height')
plt.xlim(-0.4, 1.4)

# changing x axis ticks
# plt.xticks([0.1, 0.4], [1.5, 2])

plt.title("Measured data")
plt.show()

# subplots
# https://matplotlib.org/api/_as_gen/matplotlib.pyplot.subplots.html
fig, ax = plt.subplots(2, 3) # rows, columns
ax[0, 0].plot(range(10), 'r') #row=0, col=0
ax[1, 0].plot(range(10), 'b') #row=1, col=0
ax[0, 1].plot(range(10), 'g') #row=0, col=1
ax[1, 1].plot(range(10), 'k') #row=1, col=1
ax[0, 0].title.set_text("first")
plt.suptitle("Subplots")
plt.show()

# subplots - other option
# x = np.random.rand(10)
# y = np.random.rand(10)

# plt.subplot(2, 2, 1)
# plt.plot(x, y)

# plt.subplot(2, 2, 2)
# plt.plot(x, y)

# plt.subplot(2, 2, 3)
# plt.plot(x, y)

# plt.subplot(2, 2, 4)
# plt.plot(x, y)
# plt.show()

# save to file - without showing!
# plt.plot(data)
# plt.savefig("plot_output.png")
# plt.close()

# clear
plt.clf()

# further possibilities
# showing images (in Numpy.py)
# 3D, animation, histogram, ...
# https://matplotlib.org/gallery/index.html