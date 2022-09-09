import numpy as np


def doubler(a):
    return a * 2


arr = np.linspace(1, 10, 10)
arr2 = map(doubler, arr)

print(arr)
arr = list(arr)
print(arr)
print(arr[0:-1:2])
print(arr[::2])
