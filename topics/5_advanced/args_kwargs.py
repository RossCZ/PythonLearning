def foo(standard_arg=None, *args):
    # args are passed as tuple
    print(type(args))

    # standard arg is first of args
    print(f"standard_arg: {standard_arg}")
    for i, arg in enumerate(args):
        print(f"{i}: {arg}")
    print()


def moo(standard_arg=None, **kwargs):
    # kwargs are passed as dict
    print(type(kwargs))

    # standard arg is still None
    print(f"standard_arg: {standard_arg}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

    # call sum function and fill its a, b and c arguments by kwargs
    print(f"sum function: {sum_abc(**kwargs)}")
    print()


def sum_abc(a, b, c):
    return a + b + c


# args: non-keyword arguments
print("*args")
foo("arg1", "abc", 42)
foo(*["arg1", "abc", 42])  # * unpack iterable operator
print()

# kwargs: keyword arguments
print("**kwargs")
moo(a=1, b=-2, c=3)
moo(**{"a": 1, "b": -2, "c": 3})  # ** unpack dictionary operator
