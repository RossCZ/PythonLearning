# import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import numpy as np

# https://matplotlib.org/

# data z numpy
# data = [3,2,1,0,1,2,3]
data1 = np.random.rand(50)
data2 = np.random.rand(50)
pts = np.random.rand(50, 2)
print(type(pts))

# zakladni plot
# plt.plot(data1, color="black")
# plt.plot(data2, color="red")

# plot settings
fig, ax = plt.subplots(figsize=(6, 3))
ax.yaxis.set_major_formatter(FormatStrFormatter('%.8f'))
plt.subplots_adjust(left=0.2, bottom=0.2, right=0.8, top=0.9)

# bodovy plot: x, y + nastaveni
# https://matplotlib.org/api/markers_api.html
# colors: #0f0f0f, (0.1, 0.3, 0.5)
plt.scatter(data1, data2, color="b", s=30, marker="s", label="blue line")
plt.scatter(pts[:, 0], pts[:, 1], color="r", s=20, marker="P", label="red line")

# legenda
plt.legend(loc="upper right")

# popisy os
plt.xlabel("width [m]")
plt.ylabel("height [m]")

# nastaveni os
plt.xlim(-0.4, 1.4)
plt.xticks([0.1, 0.2, 0.3], ["A","B","C"])

# titulek
plt.title("Measured data")

# vymazani, zavreni plotu
# plt.clf()
# plt.close()

# ulozeni do souboru
plt.savefig("plot_output.png")

# zobrazeni okna grafu
plt.show()

# subplots
# fig, ax = plt.subplots(2, 3)
# ax[0, 0].plot(range(10), "r")
# ax[1, 0].plot(range(10), "b")
# ax[0, 1].plot(range(10), "g")
# ax[1, 1].plot(range(10), "k")
# ax[0, 0].title.set_text("first plot")
# plt.suptitle("Subplots test")
# plt.savefig("plot_output.png")
# plt.show()

# dalsi moznosti: 3D, animation, histogram, ...
# https://matplotlib.org/gallery/index.html



