from math import e

# LEGB scope
# (L)ocal: inside function or class
# (E)nclosed: inside enclosing functions (nested functions)
# (G)lobal: at the uppermost level
# (B)uilt-in: reserved names (built-in modules)

# build-in scope
print(f"build-in e variable: {e}")

e = "global e variable"


def local_fn():
    e = "local e variable"
    print(e)

    # global keyword
    global f  # variable f belongs to the global scope (if commented -> error in the global scope when f is used)
    f = "global f variable set from local"

    def inner_fn(non_local=False):
        if non_local:
            nonlocal e
            print(e)
        else:
            e = "enclosed e variable"
            print(e)

    print("-> use nonlocal")
    inner_fn(True)

    print("-> dont use nonlocal")
    inner_fn()
    # inner_lvl2(True)  # attention: nonlocal e already set in the inner_lvl2 function!!!


local_fn()
print(e)
print(f)
