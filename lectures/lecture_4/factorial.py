import math

# for cyklus
cislo = int(input("Zadej cislo: "))
fact = 1
for i in range(2, cislo + 1):
    fact *= i
print(fact)

# faktorial pomoci while cyklu
cislo = int(input("Zadej cislo: "))
aktualni_cislo = 1
vysledek = 1

while aktualni_cislo <= cislo:
    vysledek *= aktualni_cislo
    aktualni_cislo += 1

print(vysledek)

# pouziti knihovny math
# print(math.factorial(cislo))





