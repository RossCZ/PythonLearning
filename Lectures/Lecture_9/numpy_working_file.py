import numpy as np
import matplotlib.pyplot as plt

# Numeric Python
# https://numpy.org/

# numpy array - basic entity in numpy
# ndarray (N-dimensional array)
# convert from Python list
hodnoty2 = [6,7,8,9,10]
data2 = np.array(hodnoty2)

hodnoty = [1,2,3,4,5]
data = np.array(hodnoty)

# random numbers
# data = np.random.rand(50)

# random 2D - ndarray
# data = np.random.rand(50, 2)

# prace s numpy array (nasobeni matic apod.)
data *= data2
print(data)
data *= 2

# linearni rozdeleni
data = np.linspace(1.0, 5.0, num=21)

# numpy array lze primo zobrazit v matplotlib
plt.scatter(data, data)
plt.show()
