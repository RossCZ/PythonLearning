# list, set, dict, generator
print("list:")
my_list = [(i+1)**2 for i in range(10)]
print(my_list)

print("set:")
my_set = {(i+1)**2 for i in range(10)}
print(my_set)

print("dict:")
my_dict = {i+1: letter for i, letter in enumerate("abeceda")}
print(my_dict)

print("generator:")
my_gen = (i for i in range(10))
print(my_gen)
print(next(my_gen))

# if
print("if clause:")
my_list = [item for item in range(10) if item % 2 == 0]
print(my_list)

# multiple
print("multiple c.:")
my_list = [(x, y) for x in range(2) for y in range(3)]
print(my_list)

# nested
print("nested c.:")
my_list = [[y**2 for y in range(x)] for x in range(10)]
print(my_list)