# Metaclass create Classes and Classes creates objects
# https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python
def classes_are_objects():
    print("Classes are objects")

    class MyClass(object):
        pass

    def echo(o):
        print(o)

    # class is an object in Python
    print(MyClass)  # MyClass
    print(type(MyClass))  # type
    print(type(MyClass()))  # MyClass
    echo(MyClass)  # pass class as an argument to a function

    # add attributes to a class
    print(hasattr(MyClass, "my_attr"))
    MyClass.my_attr = "spam"
    print(hasattr(MyClass, "my_attr"))
    print(MyClass.my_attr)

    # assign a class to a variable
    my_var = MyClass
    print(my_var())

    print(id(MyClass))  # use id of classes (since they are also objects)
    print(type(type))  # type is its own metaclass
    print()


def dynamic_creation_of_classes():
    print("Dynamic creation of classes")

    def spacetime():
        print("In the spacetime...")

    # type(name, bases, attrs) -> returns a class object
    Meta = type("Meta", (), {"answer": 42})
    print(Meta)
    meta = Meta()  # create an instance
    print(meta.answer)

    # inheritance, function attribute
    Universe = type("Universe", (Meta,), {"spacetime": spacetime})
    print(Universe.answer)  # attribute is inherited
    # Meta.spacetime()  # error: attribute not in base class
    Universe.spacetime()
    print()


def class_attribute():
    print("Class attribute")
    number = 35
    print(number.__class__)
    text = "abc"
    print(text.__class__)
    function = lambda x: x * 2
    print(function.__class__)
    class Egg:
        pass
    egg = Egg()
    print(egg.__class__)

    # class of class is always type
    print(number.__class__.__class__)
    print(text.__class__.__class__)
    print(function.__class__.__class__)
    print(egg.__class__.__class__)
    print()


def metaclasses():
    print("Metaclasses")

    class CapitalizedAttrMetaclass(type):
        # __new__ is called before __init__ when the class is defined
        def __new__(mcs, class_name, class_parents, class_attributes, **kwargs):
            print(f"__new__: {class_name}, {class_parents}, {class_attributes}")
            capitalized_attrs = {
                attr if attr.startswith("__") else attr.capitalize(): attr_value
                for attr, attr_value in class_attributes.items()
            }
            print(f"class keyword arguments: {kwargs}")
            # e.g. check number of parents, parent types, class attributes, ...
            # return type(class_name, class_parents, capitalized_attrs)
            return super().__new__(mcs, class_name, class_parents, capitalized_attrs)

    # metaclass keyword, __new__ is called
    # Note: keyword arguments in class definitions: https://dev.to/marvintensuan/how-to-put-keyword-arguments-in-your-python-class-definitions-864
    class SpamAndEggs(metaclass=CapitalizedAttrMetaclass, kwarg1=True):
        spam = "spam!"
        eggs = "eggs!"

    print()
    se = SpamAndEggs()  # __init__ is called
    print(se.Spam)  # capitalized attribute
    # print(se.spam)  # error

    # some attributes of the class
    print(se.__class__.__name__)
    print(se.__class__.__basicsize__)
    print()


def metaclasses_practically():
    from functools import wraps

    print("Metaclasses practically")

    class Debugger(type):
        """Debugger metaclass to enable debugging functionality for subclasses functions."""
        def __new__(mcs, class_name, class_parents, class_attributes):
            class_object = super().__new__(mcs, class_name, class_parents, class_attributes)
            class_object = mcs.debugmethods(class_object)
            return class_object

        @staticmethod
        def debugmethods(class_object):
            for key, value in vars(class_object).items():
                if callable(value):  # for callable attributes (i.e. functions) wrapp using debug decorator
                    setattr(class_object, key, Debugger.debug(value))
            return class_object

        @staticmethod
        def debug(func):
            """Debugging decorator."""
            @wraps(func)
            def wrapper(*args, **kwargs):
                print(f"|DEBUG| Method name: {func.__qualname__}")
                return func(*args, **kwargs)

            return wrapper

    # Debugger functionality is applied to all subclasses using a metaclass argument
    # decorators would have to be added to each class separately
    class Base(metaclass=Debugger):
        pass

    class CalcScalar(Base):
        def add(self, x, y):
            return x + y

    class CalcMatrix(CalcScalar):
        def matmul(self, x, y):
            return x * y

    calc_scalar = CalcScalar()
    calc_matrix = CalcMatrix()
    print(calc_scalar.add(2, 3))
    print(calc_matrix.matmul(2, 3))
    print()

    # many libraries use metaclasses: do hard work behind the scenes and expose only a simple API
    # e.g. ORM (Object-Relational Mapping)
    # however, most of the time, simpler solutions can be used: decorators, monkey patching


# *** driver code ***
classes_are_objects()
dynamic_creation_of_classes()
class_attribute()
metaclasses()
metaclasses_practically()
