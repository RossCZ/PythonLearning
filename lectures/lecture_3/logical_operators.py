
podm_a = True # 1
podm_b = False # 0

# 1 and 0 -> 0
op_and = podm_a and podm_b

# 1 or 0 -> 1
op_or = podm_a or podm_b

# 1 and not(0)
op_not = podm_a and not podm_b

print(op_and)
print(op_or)
print(op_not)

# priklad cislo b je vetsi nez 0 a mensi nez 5
b = 6
c = 3
if b > 0 and b < 5:
    # 1 and 1
    # 1
    print("v mezich")
else:
    print("mimo meze")


# skladani podminek
if b > 0 and (b < 5 or c == 3):
    # 1 and (0 or 1)
    # 1 and 1
    # 1
    print("v mezich 1")
else:
    print("mimo meze 1")

# jiny zapis toho nahore
podm_c = (b < 5 or c == 3)
if b > 0 and podm_c:
    # 1 and (0 or 1)
    # 1 and 1
    # 1
    print("v mezich 1")
else:
    print("mimo meze 1")


# jine zavorky -> jine poradi vyhodnocovani podminek
if b > 0 and b < 5 or c == 3:
    # (1 and 0) or 1
    # 0 or 1
    # 1
    print("v mezich 2")
else:
    print("mimo meze 2")





