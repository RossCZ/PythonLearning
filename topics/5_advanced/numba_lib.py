from numba import jit
import numpy as np
import time


# Numba: https://numba.pydata.org/numba-doc/latest/user/5minguide.html
matrix = np.ones(int(1e7)).reshape(1000, -1)


def python_fn(arr):
    # numpy code only - avoid using python lists, etc.
    res = 0.0
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            res = np.exp(np.cos(np.sin(np.tan(np.cosh(np.arctan(arr[i, j] ** 2))))))
    return res


# # Decorator: Function to be compiled and run in machine code
# @jit(nopython=True)  # or @njit
# def compiled_fn(arr):
#     ...

# or compile the existing python function
compiled_fn = jit(nopython=True)(python_fn)

# python function
start = time.time()
python_fn(matrix)
time_py = time.time() - start
print(f"Time (pure Python): {time_py} s")

# first run
start = time.time()
compiled_fn(matrix)
time_comp = time.time() - start
print(f"Time (including compilation time): {time_comp} s")  # including compile time

# next runs
start = time.time()
compiled_fn(matrix)
time_fast = time.time() - start
print(f"Time (after compilation) = {time_fast} s")  # executed from cache

print(f"Speedup: {time_py / time_fast:.1f}x")  # once compiled

# vectorization (@vectorize) of scalar computation can be even faster
# even more speedup is achieved by parallelization

# Output for matrix size 1e7
# Time (pure Python): 55.151488065719604 s
# Time (including compilation time): 0.36969828605651855 s
# Time (after compilation) = 0.010370254516601562 s
# Speedup: 5318.2x
