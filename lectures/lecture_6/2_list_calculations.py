import sys

my_values = [ 1, 2, 3, 4, 5 ]

# vypocet statistickych hodnot: suma, minimum, maximum, prumer, ...
suma = 0
maximum = -sys.maxsize
print(maximum)

for value in my_values:
    # suma
    suma += value

    # maximum
    if value > maximum:
        maximum = value

average = suma / len(my_values)

print(suma)
print(maximum)
print(min(my_values))
print(average)


