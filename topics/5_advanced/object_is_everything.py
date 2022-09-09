# Everything is an object in Python
def moo(obj):
    print(f"Hello {obj}")


a = 42
a = "abc"

print(type(a))
print(isinstance(a, object))  # object is base class of everything
print(object())  # initialize object instance
print(a.__str__())
print(a.__add__("d"))

print()
print("Globals:")
moo(a)
globals()["moo"].__call__(a)
print(globals())  # returns dictionary of current global symbol table

# object documentation
print()
print("--" * 16)
print(a.__doc__)
