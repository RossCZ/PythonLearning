
# e.g. user input
inpt = "25.8gd"
inpt = input("type number: ")

try:
    value = float(inpt)
	raise ValueError("cislo neni kladne")
    result = value * 2.0
    print(f"{inpt} * 2 = {result}")
except ValueError as e:
    print("value error")
    print(e)
except Exception as e:
    print("general exception")
    print(e)
    print(e.with_traceback)
except:
    print("Oh Jeez!")
    print("wrong input")
