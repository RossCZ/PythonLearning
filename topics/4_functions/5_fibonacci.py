def fib1(n):
    fib_numbers = [0, 1]
    for _ in range(n-1):
        # zde sečtu poslední dva elementy fib. posloupnosti
        fib_next = fib_numbers[-1] + fib_numbers[-2]
        fib_numbers.append(fib_next)
    nth_fib_num = fib_numbers[-1]
    return nth_fib_num


def fib(n):
    # použití rekurze
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_next = fib(n-1) + fib(n-2)
        return fib_next


result = fib(2)
print(result)
