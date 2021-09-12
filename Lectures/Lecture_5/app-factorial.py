import math

while True:
    cislo = int(input("Zadej cislo: "))
    print(f"Faktorial cisla {cislo} je {math.factorial(cislo)}")

    konec = input("Nový výpočet? (Y/N) ")

    if konec.lower() == "n":
        print("konec...")
        break


