class Stock:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Stock value: {self.value}"

    def __add__(self, other):
        return Stock(self.value + other.value)


s1 = Stock(3)
s2 = Stock(2)
print(s1)
print(s2)
print(s1 + s2)
