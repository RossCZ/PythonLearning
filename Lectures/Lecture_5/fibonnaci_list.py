fib_numbers = [ 0, 1 ]

for i in range(50):
    # fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
    fib_numbers.append(fib_numbers[len(fib_numbers) - 1] + fib_numbers[len(fib_numbers) - 2])

print(fib_numbers)
