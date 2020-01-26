import math
import matplotlib.pyplot as plt


# funkce pro rekurzivni vypocet cisla na pozici n ve fibonacciho posloupnosti
def fibonacci(n): 
    if n < 0: 
        print("Incorrect input") 
    # First Fibonacci number is 0 
    elif n == 1: 
        return 0
    # Second Fibonacci number is 1 
    elif n == 2: 
        return 1
    else: 
        return fibonacci(n - 1) + fibonacci(n - 2)

# funkce pro dynamicky vypocet cisla na pozici n
# doplnuje pole jiz vypoctenych cisel, takze je nemusi pocitat znovu
def fibonacci_dyn(n, fib_array): 
    if n < 0: 
        print("Incorrect input") 
    elif n <= len(fib_array): 
        return fib_array[n - 1] 
    else: 
        temp_fib = fibonacci_dyn(n - 1, fib_array) + fibonacci_dyn(n - 2, fib_array)
        fib_array.append(temp_fib) 
        return temp_fib 


# fibonnaciho posloupnost pomoci cyklu
def fibonnaci_list_loop(n):
    fib_array = [0, 1]
    while len(fib_array) < n:
        fib_array.append(fib_array[-1] + fib_array[-2])
    return fib_array


# naplneni listu fibonacciho posloupnosti volanim rekurzivni funkce (pomale pro velka cisla)
def fibonacci_list(n):
    fib_nums = []

    if n < 0: 
        print("Incorrect input") 
    else:
        for i in range(1, n + 1):
            fib_nums.append(fibonacci(i))
    
    return fib_nums


# graficke zobrazeni fibonnaciho spiraly - zjednodusene
def graphical_fibonnaci(n):
    fib_array = fibonnaci_list_loop(n)

    x, y = [], []
    for i in range(1, n):
        # angle = i * math.pi / 2.0
        angle = i * math.pi / 2.0 * 0.1
        # len = fib_array[i]
        len = math.pow(fib_array[i], 0.1)
        x.append(math.sin(angle) * len)
        y.append(math.cos(angle) * len)
    
    plt.plot(x, y)
    plt.show()


def graphical_golden_angle(n):
    x, y = [], []
    golden_angle = 2 * math.pi * 0.381966 
    for i in range(0, n):
        angle = golden_angle * i
        len = 0.1 + math.pow(0.001 * i, 0.5)
        x.append(math.sin(angle) * len)
        y.append(math.cos(angle) * len)
    
    plt.scatter(x, y, s=0.8)
    plt.show()


# ridici kod
print(fibonacci(9))
print(fibonacci_list(20))
graphical_fibonnaci(1000)


