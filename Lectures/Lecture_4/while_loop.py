# zacykleni programu!!!
# cislo = 1
# while True:
#     cislo += 1
#     print("Ahoj", cislo)

# Zpusob 1: explicitne definovany konec
konec = False
cislo = 1

while not konec:
    print(cislo)
    cislo += 1

    # ukoncovaci podminka
    if cislo > 3:
        konec = True

# Zpusob 2: ukoncovaci podminka pomoci vyrazu
cislo = 1

while cislo <= 10:
    print(cislo)

    # toto, v kombinaci s podminkou nahore, zpusobi ukonceni cyklu
    cislo += 1





