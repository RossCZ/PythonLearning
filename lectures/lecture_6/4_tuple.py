# datovy typ "tuple" - n-tice
# index: 0   1
pt1 = (3.4, 5.2)
pt2 = (1.0, 6.7)

# pristup k hodnotam stejne jako u listu pomoci indexu
print(pt1[1])

# list n-tic
my_values = [ pt1, pt2 ]
print(my_values)

# razeni pomoci uzivatelskeho klice -> lambda funkce
my_values.sort(key=lambda a: a[0])
print(my_values)

