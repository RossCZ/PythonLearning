horni_mez = int(input("Zadej horni mez: "))

for i in range(0, horni_mez + 1):
    # zobrazit jen suda cisla
    if i % 2 == 0:
        print(i)