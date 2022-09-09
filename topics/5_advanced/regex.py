import re


# regulární výrazy
print("Regular expressions:")
print(re.search(r"[a-z]+.[a-z]+@[a-z]+.[a-z]{2,4}", "hledani emailu v textu jmeno.prijmeni@mail.com, jako je tento"))
for match in re.finditer(r"[A-Z]{1}[0-9]{2}", "hledání kódového označení výrobků jako S21, A33, Z2, X007, C00"):
    print(match)
print()

# hledání a nahrazování textu
print("Search and replace:")
text = "abeceda začítá písmeny abc"
print(re.findall("ab", text))
print(re.split("\s", text, 2))  # first two spaces are used for split
print(re.sub("\s", "-", text))  # replace matches
print()

# match object
print("match object:")
m = re.search("ab", text)
print(type(m))
print(m.start(), m.end(), m.span(), m.string, m.group())