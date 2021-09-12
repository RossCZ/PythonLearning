# napiste funkci na výpočet kvadratické rovnice
# funkce bude brát parametry: a, b, c
# funkce bude vracet všechny reálné kladné kořeny (list)
def quadratic(a, b, c):
    koreny = []

    D = b**2 - 4 * a * c
    if D >= 0:
        x1 = (-b + D**0.5) / (2 * a)
        x2 = (-b - D**0.5) / (2 * a)
        koreny.append(x1)
        koreny.append(x2)

    return koreny

print(quadratic(-1, 2, 3))
print(quadratic(1, 1, 3))