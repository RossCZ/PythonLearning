from dataclasses import dataclass


@dataclass
class Bag:
    item1: str
    item2: int


# custom decorator
def flyable(func):
    def wrapper(*args):
        print(f"Fly {args[1]} {args[0].name}!")
        func(*args)

    return wrapper


@dataclass
class SuperCat:
    name: str

    @flyable
    def walk(self, where):
        print("Walk...")


bag = Bag("Deuter", 25)
print(bag)

cat = SuperCat("Bob")
cat.walk("there")
