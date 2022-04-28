# definice funkce
def kv_rovnice(a, b, c):
    # definice vnořených funkcí:
    fn_D = lambda a, b, c: b ** 2 - 4 * a * c  # lambda

    def vypocet_x(a, b, D, znam):  # standartní funkce
        x = (-b + znam * D ** 0.5) / (2 * a)
        return x
    # zde končí definice vnořených funkcí

    # zde je vlastní výpočet
    # použití definovaných vnořených funkcí
    D = fn_D(a, b, c)
    x1 = vypocet_x(a, b, D, 1)
    x2 = vypocet_x(a, b, D, -1)

    # vrátím vypočtené hodnoty z funkce
    return x1, x2

# použití (zavolání) funkce pro výpočet kv. rovnice
x1, x2 = kv_rovnice(1, 2, 3)
print(x1, x2)
print("end")
