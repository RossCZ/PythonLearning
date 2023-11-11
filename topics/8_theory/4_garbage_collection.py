import sys
import gc  # https://docs.python.org/3/library/gc.html


def scope():
    def fn():
        a = 123
        print(a)
        # end of fn scope

    b = 456
    print(b)
    fn()
    # print(a)  # variable 'a' is not defined in this scope


def ref_count():
    # (in ipython console)
    var = "my-variable"  # 1st reference
    # arr = [var, var]  # other references
    # del arr
    count = sys.getrefcount(var)  # 2nd reference
    print("Variable 'a' reference count:", count)


def gc_example():
    print(gc.get_count())
    gc.collect()
    print(gc.get_count())


# examples:
scope()
print()
ref_count()
print()
gc_example()

