muj_list = [1, 2, 3, 4]
konst = 5

print("globalni scope")

for hodnota in muj_list:
    lokalni_konstanta = 2
    print("uvnitr for cyklu", lokalni_konstanta)

    if hodnota > lokalni_konstanta:
        print("pravda", hodnota)

print("zpet v globalni scope")

# pozor, narozdil od jinych programovacich jazyku 
# je lokalni konstanta viditelna i mimo scope!
# https://stackoverflow.com/questions/10563613/does-python-officially-support-reusing-a-loop-variable-after-the-loop
# toto ale neplati pro funkce, viz priste
print(lokalni_konstanta)


