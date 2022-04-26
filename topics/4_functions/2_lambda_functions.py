# define lambda (anonymous) functions
hello_lambda = lambda: print("hello lambda")
print_fn = lambda x: print(f"value is {x}")
power_fn = lambda x, pow: x ** pow


# test lambda functions
hello_lambda()
print_fn(88)
print(power_fn(2, 3))

# list filtering
my_list = list(range(10))
print(my_list)
even_nums = list(filter(lambda number: number % 2 == 0, my_list))
print(even_nums)
