import numpy as np
import ctypes
import sys


def systems():
    a = 5
    print(f"decimal: {a}")
    print(f"binary: {bin(a)}")  # 1 * 2^2 + 0 * 2^1 + 1 * 2^0 = 4 + 0 + 1 = 5
    print(f"hexadecimal: {hex(15)}")  # a, b, c, d, e, f (10-15)

    # 2 bits
    # | 0,0 | 0,1 | 1,0 | 1,1 | = 2^2 = 4 combinations
    for i in range(31):
        print(f"2^{i}: {2**i:_}")

    # 1 Byte == 8 bits
    # GB (Gygabyte: 1e9 or 1 073 741 824 bytes) =  vs Gb (Gigabit: 1e9 bits)
    # https://www.mixvoip.com/article/what-is-the-difference-between-gb-and-gb


def int_32():
    a = 10  # int32
    print(type(a))

    print(f"int32 Bytes: {ctypes.sizeof(ctypes.c_int)}")
    # int4, int8, int16, int32, int64

    print(np.iinfo(int))
    int32_min = np.iinfo(int).min
    int32_max = np.iinfo(int).max
    print(f"int32 values: {int32_max - int32_min:_}")  # + sign bit
    print(f"2^32 - 1: {2 ** 32 - 1:_}")

    print("int64")
    print(sys.maxsize, 2**63 - 1)  # uint64


def float_64():
    # https://en.wikipedia.org/wiki/Double-precision_floating-point_format
    # 1 bit: sign bit, 11 bits: exponents, 52 bits: fraction (significant precision)
    print(sys.float_info)
    print(1.1234567890123456_789)  # 17 significant digits:  _789.. not stored
    print(112345678901234567.89)  # 1.1234567890123456e+17  (112345678901234560.0) (arbitrary decimal point, always 17 sig. digits)


# systems()
# int_32()
float_64()
