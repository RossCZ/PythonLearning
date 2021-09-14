# naplnte list hodnotami 1...n
import random

my_values = []
n = 100

for i in range(1, n + 1):
    # my_values.append(i)

    # vytvori nahodne cislo od a-1 do b
    val = random.randint(1, 10)
    my_values.append(val)


print(my_values)