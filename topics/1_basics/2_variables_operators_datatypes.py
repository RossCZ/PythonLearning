import math


# # promenne (leva strana od "="), nazev si volime
# # hodnota (prava strana od "=")
# a1 = 1 + 1
# b1 = 2
# moje_promenna_jedna = a1 + b1
# # print(moje_promenna_jedna)

# # zakladni datove typy
# boolean = True # bool
# cele_cislo = 1 # int
# desetinne_cislo = 1.5 # float
# complexni_cislo = 2.5 + 1.5j # complex
# text = "Hello world" # string

# # zjisteni typu
# print(type(complexni_cislo))
# print(complexni_cislo)

# # prace s typy
# a = 1
# b = "2"
# c = a + int(b)
# print("c je:", c)
# # d = ... # jak?
# print("d je:", d) # output: "12"

# operatory
# aritmeticke o. (+, -, *, /, ...)
# a = 15.0
# b = a % 6.0 # 3
# print(b)

# c = b ** 2 # 9
# print(c)

# d = (1.0 + c) / b
# print(d)

# e = 1
# e = 2
# e = 2 * e
# print(e)

# # vyuziti modulu "math" - složitější matematické operace
# print(math.sqrt(c)) # c ** 0.5

# Příklad: pravouhly trojuhelnik, vypocet delky přepony (a, b: známe; c = ?)
# a = 3.0
# b = 4.0
# c = ((a ** 2.0) + (b ** 2.0)) ** 0.5
# print(c)

# a = 3
# b = 2
# c = b / a
# print(c)

# přiřazovací o.("=")
# a = 1
# a += 1 # a = a + 1
# a *= 3 # a = a * 3
# print(a)

# porovnávací o.
# a = 1
# b = 2
# print(a > b)
# c = a == b
# print(c)
# print(a == 1)

# d = 4
# e = 4
# print(e >= d)
# print(e != d + 1)

# logic1 = True
# logic2 = False

# print(logic1 != logic2)

# Priklad: tajna promenna A = 4, input("Hadej cislo")
tajna_promenna = 4
odhad = input("Hadej cislo:")
# pozor: nemuzu porovnavat typ "int" s typem "string", nutno pretypovat!
# print(tajna_promenna == int(odhad))

# odhad je roven tajne promenne (if ...)
if tajna_promenna == int(odhad):
    print("Trefa")
else:
    print("Cislo jsi neuhodl")
















