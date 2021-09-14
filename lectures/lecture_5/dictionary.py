
# struktura na bázi párů: klíč - hodnota
# klíče musí být unikátní (nelze více klíčů v jednom slovníku)
# více zde: https://www.w3schools.com/python/python_dictionaries.asp
slovnik = {
    "aaa": 100,
    "bbb": 200,
    "ccc": 300
}

# procházení slovníku
for item in slovnik.items():
    print(item)

for key, value in slovnik.items():
    print(f"key: {key}, value: {value}")

# pristup k polozkam
print(slovnik["aaa"])

# funkce get vrátí None když klíč neexistuje
polozka = slovnik.get("ddd")
print(polozka)

# prepsani klice
slovnik["aaa"] = 400

# pridani klice
slovnik["eee"] = 500
print(slovnik)

