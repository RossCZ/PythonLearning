
# list
# zakladni typ kolekce v Pythonu i jinde
# indexy:   0  1  2  3  4
# indexy_r:-5 -4 -3 -2 -1 
hodnoty = [ 1, 2, 3, 4, 5 ]

print(hodnoty)

# index
# pozor zacina 0
# tj. posledni index = pocet polozek - 1
prvni = hodnoty[0]
print(prvni)

print(hodnoty[-1])

# range
print(hodnoty[1:4])
print(hodnoty[1:-1])

# delka listu (pocet polozek)
print(len(hodnoty))

# zmena hodnoty
hodnoty[0] = "ahoj"
print(hodnoty)

# pridani hodnoty
hodnoty.append(3.14)
print(hodnoty)

# prochazeni listu
for hodnota in hodnoty:
    print(hodnota)
