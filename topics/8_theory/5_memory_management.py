# https://realpython.com/python-memory-management/
# https://www.geeksforgeeks.org/id-function-python/

# stack vs heap
# https://www.geeksforgeeks.org/stack-vs-heap-memory-allocation/
# https://docs.python.org/3/c-api/memory.html
# https://stackoverflow.com/questions/14546178/does-python-have-a-stack-heap-and-how-is-memory-managed


def memory_address():
    # id: memory address
    a = 1  # int32
    b = 2
    print(id(a), id(b), id(b) - id(a))

    # https://realpython.com/linked-lists-python/#performance-comparison-lists-vs-linked-lists
    my_list = [1, 2, 3]
    print(id(my_list), id(my_list[0]), id(my_list[1]), id(my_list[2]), id(my_list[2]) - id(my_list[0]))


def references():
    # https://www.geeksforgeeks.org/mutable-vs-immutable-objects-in-python/
    # https://towardsdatascience.com/assignment-shallow-or-deep-a-story-about-pythons-memory-management-b8fad87bfa6c
    spam = "spam"
    list1 = [spam]
    list2 = [spam, spam]  # points to the same objects unless their value is changed
    list3 = list2  #  .copy()  # points to the same list variable without copying
    print(list2 is list3, id(list2) == id(list3))  # if copied: False
    print(id(spam), id(list1), id(list1[0]), id(list2), id(list2[0]), id(list3), id(list3[0]))

    spam = "eggs"
    eggs = spam  # new variable (points to the same address unless the value is changed)
    print(id(spam), id(list1[0]), id(eggs))

    list1[0] = "ham"  # changes value only in list1
    print(id(spam), id(list1[0]), id(list2[0]))

    list2[0] = "ham"  # change values in both list1 and list2 (when not copied)
    print(list1, list2, list3)


# memory_address()
# print()
references()
