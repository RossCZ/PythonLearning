import random

my_values = []

for i in range(0, 100):
    my_values.append(random.randint(1, 100))

print(my_values)

# razeni listu vzestupne
my_values.sort()
print("")
print(my_values)
print("")

# razeni listu sestupne
my_values.sort(reverse=True)
print(my_values)


