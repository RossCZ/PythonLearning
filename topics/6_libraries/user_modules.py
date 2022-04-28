import my_library.helper_functions as hf
import my_library.numerical_methods as nm
# import my_package.helper as hlp
from my_package import helper as hlp

hf.funkce1()
hf.funkce2()
hf.funkce3()

print(nm.is_less(1, 2))
print(nm.is_less(3, 2))

var = nm.is_less(3, 2)

rand = hlp.get_random()
print(rand)






