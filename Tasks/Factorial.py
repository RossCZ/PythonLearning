num = input("Enzer a number: ")

# rekurzivni volani funkce pro vypocet faktoriálu čísla
def factorial(n):
    if n == 1:
        return n
    elif n < 1:
        return ("n/a")
    else:
        return n * factorial(n - 1)

print(factorial(int(num)))