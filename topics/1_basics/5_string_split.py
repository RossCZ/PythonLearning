def example1():
    txt = "a b c d"
    txt2 = "a-b-c-d"

    lst = txt.split(" ")
    print(lst)

    lst2 = txt2.split("-")
    for character in lst2:
        print(character)


def example2():
    data = "1,25.6,-8.3"
    print(data[1])

    data_splitted = data.split(",")
    print(data_splitted[1])


example1()
example2()
