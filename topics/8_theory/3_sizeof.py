import sys
import numpy as np
import time
import psutil
import ctypes


# https://www.geeksforgeeks.org/data-types-in-c/
print("Basic types")
print("int32:", ctypes.sizeof(ctypes.c_int))  # int32: 32-bit: 4 B  (Python int)
print("float32:", ctypes.sizeof(ctypes.c_float))  # float32: 32-bit: 4 B
print("float64:", ctypes.sizeof(ctypes.c_double))  # float64: 64-bit: 8 B  (Python float)
print("Python float (object):", sys.getsizeof(float()))  # 24 B (whole class)
print()

print("Arrays")
values = [ctypes.c_int(i) for i in range(4)]
arr = (ctypes.c_int * len(values))(*values)  # C-array 4*4=16 B
print(f"{ctypes.sizeof(ctypes.c_int)} * {len(arr)} = {ctypes.sizeof(arr)} B")
print(f"8 * 1000 = {sys.getsizeof(np.ones(1000)):_} B")  # ~8 kB
print()

print("Large dataset")
mem1 = psutil.virtual_memory().available

# 1e9 values: 100 sensors, 1 measurement per second: 3.7 months
arr = np.random.rand(int(1e7), 100)  # 8*1e9 = 8 GB

mem2 = psutil.virtual_memory().available

print(f"{sys.getsizeof(arr):_} B")
print(f"{(mem1 - mem2):_} B")
time.sleep(3)

# del arr
print("end: memory released")
