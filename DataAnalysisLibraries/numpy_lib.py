import numpy as np
from skimage import io
import matplotlib.pyplot as plt

# Numeric Python
# https://numpy.org/
# https://towardsdatascience.com/the-ultimate-beginners-guide-to-numpy-f5a2f99aef54 

# data
# manual
data = [ 3, 2, 1, 0, 1, 2, 3 ]
print(data)

# numpy array - basic entity in numpy
# ndarray (N-dimensional array)
# convert from Python list
data = np.array([1, 2, 3])
print(type(data))
print(data)

# random numbers
data = np.random.rand(50)
print(data)

# random 2D - ndarray
data = np.random.rand(50, 2)
print(data)

# linear division
data = np.linspace(1.0, 5.0, num=21)
print(data)

# zeroes
data = np.zeros(3)
print(data)

# ones
data = np.ones(10)
print(data)

# empty (zeroes), less common
data = np.empty(5)
print(data)

# shape 
print(data.shape)
data.shape = (5, 1)
print(data.shape)

# random
np.random.seed(0)
data = np.random.randint(10, size=6)
print(data)

# indexing
print(data[0])
print(data[1:-1])

# 2D array - image example
# read image as numpy array
photo = io.imread("..Data\landscape.jpg")
print(type(photo))
print(photo.shape)
plt.imshow(photo)

# flip
# plt.imshow(photo[::-1])

# mirror
# plt.imshow(photo[:, ::-1])

# section (y range, x range)
# plt.imshow(photo[50:100, 520:620])

# slicing: every other row and column
# extended slices: https://stackoverflow.com/questions/3453085/what-is-double-colon-in-python-when-subscripting-sequences
# plt.imshow(photo[::2, ::2])

# transposing array
plt.imshow(photo[:,:,0].T) # color change?
plt.show()

# apply numpy functions
photo_sin = np.sin(photo)
print(photo_sin)

# quick statistics
print(np.sum(photo))
print(np.prod(photo))
print(np.mean(photo))
print(np.std(photo)) # standard deviation
print(np.var(photo)) # variance
print(np.min(photo))
print(np.max(photo))
print(np.argmin(photo)) # index value of minimum
print(np.argmax(photo)) # index value of maximum

# logic operations with arrays
z = np.array([1, 2, 3, 4, 5])
# array of logic values [True, False, ...]
print(z < 3)
print(z > 3)

# slicing the original array
print(z[z > 3])

# photo masks
photo_masked = np.where(photo > 100, 255, 0)
# plt.imshow(photo_masked)
# plt.show()

# aritmethic operations with arrays
a_array = np.array([1, 2, 3, 4, 5])
b_array = np.array([6, 7, 8, 9, 10])

print(a_array + b_array)
print(a_array + 30)
print(a_array * b_array)
print(a_array * 3)

# dot product
print(a_array @ b_array)

# sorting
x = np.array([2, 1, 4, 3, 5])
print(np.sort(x))

# jednotkova matice
np.eye(5)

# one hot vector [0, 1, 0, 0, 0]
np.eye(5)[2]