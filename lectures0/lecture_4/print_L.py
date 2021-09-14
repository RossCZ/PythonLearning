# priklad: print L
# user input - L size
# e.g. size = 3
# output:
# L
# L
# LLL
size_L = int(input("Zadej velikost L: "))
znak = input("Zadej znak: ")

for i in range(size_L):
    if i == size_L - 1:
        print(znak * size_L)
    else:
        print(znak)


# string multiplication
# print('-' * 3)



