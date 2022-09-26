from numba import jit
import numpy as np
import time


# Numba: https://numba.pydata.org/numba-doc/latest/user/5minguide.html
matrix = np.ones(10000000).reshape(1000, -1)


# Function to be compiled and run in machine code
@jit(nopython=True)
def compiled_fn(arr):
    res = 0.0
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            res = np.exp(np.cos(np.sin(np.tan(np.cosh(np.arctan(arr[i, j] ** 2))))))
    return res


# first run
start = time.time()
compiled_fn(matrix)
time1 = time.time() - start
print(f"Time (including compilation time): {time1} s")  # including compile time

# next runs
start = time.time()
compiled_fn(matrix)
time2 = time.time() - start
print(f"Time (after compilation) = {time2} s")  # executed from cache

print(f"Speedup: {time1 / time2:.1f}x")
