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
print(globals())  # dictionary of the module namespace (global symbol table)
print()

# object documentation
print()
print("--" * 16)
print(a.__doc__)
print()

# globals, locals, vars
print("Note: locals, vars:")
print(locals())  # dictionary of the current namespace
print(vars())  # dictionary of the current namespace


class Magic(object):
    a = "aaa"
    b = "bbb"


mag = Magic()
vrr = vars(mag)  # dictionary of the argument
vrr["c"] = "ccc"
print(mag.c)
