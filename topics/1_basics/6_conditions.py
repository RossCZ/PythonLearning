# Podminky

# hlavni vetev programu
print("start")

a = 1  # int
logic = a > 0  # bool

# logicka podminka
# if "bool":
if logic:
    print("větev B")
    print("složitý výpočet...")
elif a > 2:  # else if
    print("větev D")
elif a > 5:  # else if
    print("větev E")
else:
    print("větev C")
    print("ještě složitější výpočet...")

# zpatky v hlavni vetvi programu
print("end")


# vnořená podmínka
a = 3
if a > 0:
    print("vetsi nez 0")
    if a > 5:
        print("vetsi nez 5")
    else:
        print("mensi nez 5")
else:
    print("mensi nez 0")