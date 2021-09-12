
# vstupni parametry (napr.)
tol = 0.0001 # tolerance s jakou je porovnani na nulu provedeno
a = -0.0005 # napr cislo 0.0000001 je inzenyrska nula (pro vypocty)

# je cislo "a" rovno 0.0 s toleranci "tol"?
if abs(a) < tol:
    print("cislo je nula")
else:
    print("cislo neni nula")


