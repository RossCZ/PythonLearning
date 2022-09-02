# Generators and coroutines
def generator(n):
    for num in range(1, n):
        yield num ** 2


def division_coroutine(divider):
    print(f"Divider: {divider}")
    try:
        while True:
            quotient = yield
            print(quotient / divider)
    except GeneratorExit:
        print("Dividing finished...")


print("Generators:")
g = generator(10)
print(next(g))
print(next(g))

print("Coroutines:")
# Create a coroutine
division_by_10 = division_coroutine(10)

# Start a coroutine execution and proceed to the first yield
division_by_10.__next__()

# Send inputs to the coroutine
division_by_10.send(100)
division_by_10.send(500)
division_by_10.send(1000)

# close the coroutine
division_by_10.close()
