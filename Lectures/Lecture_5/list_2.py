
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