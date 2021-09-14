# priklad: seznam studentu: jmeno, vek
# seradit od nejmladsiho po nestarsiho
studenti = [
    ("Tomas", 25),
    ("Jana", 18),
    ("Pavel", 31),
    ("Honza", 22),
    ("Klara", 27) # bacha, na konci uz neni carka
]

print(studenti)
studenti.sort(reverse=False, key=lambda student: student[1])
print(studenti)