a = 9
b = 8

print(f"a = {a} ({bin(a)})")
print(f"b = {b} ({bin(b)})")

print("compare:")
print(f"a & b = {a & b} ({bin(a & b)})")
print(f"a | b = {a | b} ({bin(a | b)})")
print(f"a ^ b = {a ^ b} ({bin(a ^ b)})")    
# two's complement: ~x = (-1 * (x+1))
# e.g. 9: ~(1001) = 0110 - 1 = 0101 -> 1010 = 10 -> -10
print(f"~a = {~a} ({bin(~a)})")

print("shift:")
print(f"a >> 1 = {a >> 1} ({bin(a >> 1)})")
print(f"a << 1 = {a << 1} ({bin(a << 1)})")



