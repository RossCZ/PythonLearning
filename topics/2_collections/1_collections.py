# LIST
my_list = []
my_list = list(range(10))

my_list.append(1)
my_list.remove(2)
print(my_list[3])

# iterace přes všechny elementy
for item in my_list:
    print(item)

print(len(my_list))

# kontrola, jestli index existuje
index = 9
if len(my_list) > index:
    print(my_list[index])

print(my_list[-2:])  # slicing

# DICTIONARY - kolekce párů (klíč: hodnota)
my_dict = {}
my_dict = {
    123: "P. Novák",
    124: "M. Veselá"
}
print(my_dict[123])
print(my_dict.keys())

# SET - kolekce unikátních hodnot
my_set = {"a", "b", "c"}
my_set.update("c")
print(my_set)

# TUPLE (n-tice)
x = (1.2, 1.3)
print(x)
x1, x2 = x  # rozbalení n-tice
print(x1)
