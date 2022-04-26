# výpočet kvadratické funkce
a = float(input("Zadej parametr a: "))
b = float(input("Zadej parametr b: "))
c = float(input("Zadej parametr c: "))

D = b ** 2 - 4 * a * c

if D > 0:
    x1 = (-b + D ** 0.5) / (2 * a)
    x2 = (-b - D ** 0.5) / (2 * a)
    print(f"Nalezeny kořeny {x1} a {x2}")
elif D == 0:
    x1 = (-b + D ** 0.5) / (2 * a)
    print(f"Nalezen kořen {x1}")
else:
    print("Reálný kořen nenalezen")