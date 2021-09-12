# bezparametrická funkce bez návratové hodnoty
def say_hello():
    print("hello from function")

# funkce parametrem bez návratové hodnoty
def say_hello_to_someone(someone):
    print(f"hello {someone}")

# funkce s třemi parametry bez návratové hodnoty
def my_funciton(param1, param2, param3):
    print(f"p1 {param1}, p2 {param2}")

# funkce se dvěma parametry s návratovou hodnotou
def suma(a, b):
    # vypocet
    vysl = a + b
    koreny = []
    return vysl

# volání funkcí
say_hello()
say_hello()
say_hello()
say_hello_to_someone("Tom")
say_hello_to_someone("Jana")
my_funciton(1, 2, 3)

vysledek = suma(1, 2)
print(vysledek)




