import random

# vygenerujte matici nahodnych cisel o velikosti n (zadane uzivatelem)
# n-radku, n-sloupcu
# -> list v listu
n = int(input("Zadej velikost: "))
matice = []  # [[]]

for row in range(n):
    radek = []
    for value in range(n):
        radek.append(random.randint(1, 10))
    matice.append(radek)

# print(matice)

for row in matice:
    print(row)


print(matice[1][1])






