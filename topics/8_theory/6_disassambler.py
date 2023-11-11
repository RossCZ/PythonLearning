import dis  # https://docs.python.org/3/library/dis.html
# https://stackoverflow.com/questions/12673074/how-should-i-understand-the-output-of-dis-dis


def foo(x, y):
    return x, y


def fn():
    x = 1
    y = 3
    return foo(x, y)


print(dis.dis(fn))
# print(dis.dis(foo))
