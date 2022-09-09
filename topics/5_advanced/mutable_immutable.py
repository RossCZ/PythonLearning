# immutable: bool, int, float, str, tuple, frozenset
# mutable: list, set, dict

# immutable types
print("Immutable types:")
my_tuple = (1, 2, 3)
your_tuple = my_tuple
# my_tuple[1] = 4  # error (cannot change, only reassign)
print(id(my_tuple), id(your_tuple))  # same
your_tuple += (4, 5)  # concatenate two tuples -> creates new variable
print(id(my_tuple), id(your_tuple))  # different
print(my_tuple, your_tuple)
print(hash(my_tuple))  # hashable
print()

# mutable types
print("Mutable types:")
my_list = [1, 2, 3]
your_list = my_list
my_list[1] = 4

print(id(my_list), id(your_list))  # same (pointer to the same location in the memory)
print(my_list, your_list)
# print(hash(my_list))  # error (mutable types not hashable)
print()


# don't use mutable default arguments
def root_of_all_evil(mutable_def_arg=[]):
    mutable_def_arg.append("abc")  # changes mutable default argument
    result = ["stuff"] + mutable_def_arg
    return result  # mutable_def_arg


print("Mutable default arguments:")
print(root_of_all_evil())
print(root_of_all_evil())
print(root_of_all_evil())
