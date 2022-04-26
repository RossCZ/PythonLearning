fn = lambda a, b, c: b ** 2 - 4 * a * c
filtr = lambda x: x > 0

print(fn(10, 2, 3))

# vnořené definice funkcí
def fn_1():
    # fn_3 je definováno uvnitř fn_1
    def fn_3():
        pass
    
    # použití vnořené funkce
    fn_3()
    pass

def fn_2():
    pass