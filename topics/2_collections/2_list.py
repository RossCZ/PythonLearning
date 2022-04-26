# LIST - ÚVOD
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


# LIST - DOPLNĚNÍ
# list v Pythonu muze obsahovat jakekoli datove typy, treba i jiny list
muj_jiny_list = [ 0.1, 0.2, 0.3, 0.4 ]
muj_list = [ "ahoj", "hello", 3.14, 1, muj_jiny_list ]

# zjisteni jestli je dana polozka v listu
if "ahoj1" in muj_list:
    print("je v listu")
else:
    print("neni v listu")

print(muj_list)

# matice - list v listu
matice = [ [1, 2], [3, 4] ]
print(matice)

for radek in matice:
    for hodnota in radek:
        print(hodnota)