txt = "a b c d"
txt2 = "a-b-c-d"

lst = txt.split(" ")
print(lst)

lst2 = txt2.split("-")
for character in lst2:
    print(character)


