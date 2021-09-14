#Podminky

# hlavni vetev programu
print("start")

a = 1 # int
logic = a > 0 # bool

# logicka podminka
# if "bool":
if logic:
    print("vetev B")
    print("slozity vypcet...")
elif a > 2: # else if
    print("vetev D")
elif a > 5: # else if
    print("vetev E")
else:
    print("vetev C")
    print("jeste slozitejsi vypcet...")

# zpatky v hlavni vetvi programu
print("end")
