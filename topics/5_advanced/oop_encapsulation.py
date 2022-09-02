class Base:
    __name = "blank"  # private
    _size = 10  # protected (only a convention - can be accessed from the outside)

    def introduce(self):
        print(self.__name, self._size)


class Foo(Base):
    def introduce(self):
        print(self._size)
        # print(self.__name)  # cannot access base class private attribute

    # magic method
    def __str__(self):
        pass


f = Foo()
f.introduce()

b = Base()
b.introduce()
print(b._size)  # can access
# print(b.__name)  # error
