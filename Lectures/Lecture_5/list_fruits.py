# inicializace prázdného listu
kosik = []

while True:
    # zde bude pridavani polozek do kosiku
    polozka = input("Vyber položku: ")

    # overeni ze dana polozka v kosiku jeste neni
    if polozka not in kosik:
        kosik.append(polozka)
        print("Polozka pridana")
    else:
        print("Kosik jiz obsahuje danou polozku")

    # zobrazeni kosiku
    print(f"Kosik obsahuje: {kosik}")
    print(f"Posledni pridana polozka: {kosik[-1]}")

    # ukonceni programu
    konec = input("Nový výběr? (Y/N) ")
    if konec.lower() == "n":
        print("konec...")
        break