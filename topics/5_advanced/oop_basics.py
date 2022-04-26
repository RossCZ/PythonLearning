import numpy as np
import matplotlib.pyplot as plt


class GeometryObject:
    def __init__(self, x, y, id):
        self.position = (x, y)
        self.id = id

    def area(self):
        raise NotImplementedError

    def visualize(self):
        raise NotImplementedError

    def __str__(self):
        return f"Geometry obejct {self.id}: [{self.position[0]:.3f};{self.position[1]:.3f}]"


class Rectangle(GeometryObject):
    def __init__(self, x, y, width, height, id=None):
        super().__init__(x, y, id)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def visualize(self):
        plt.gca().add_patch(plt.Rectangle(self.position, self.width, self.height, color="b"))

    def __str__(self):
        return f"Rectangle {self.id}: [{self.position[0]:.3f};{self.position[1]:.3f}], size = {self.width:.3f} m * {self.height:.3f} m, area = {self.area():.3f} m2"


class Circle(GeometryObject):
    def __init__(self, x, y, r, id=None):
        super().__init__(x, y, id)
        self.radius = r

    def area(self):
        return np.pi * (self.radius ** 2)

    def visualize(self):
        plt.gca().add_patch(plt.Circle(self.position, self.radius, color="r"))

    def __str__(self):
        return f"Circle {self.id}: [{self.position[0]:.3f};{self.position[1]:.3f}], radius = {self.radius:.3f} m, area = {self.area():.3f} m2"


def generate_objects(num):
    # c1 = Circle(x=0, y=0, r=2, id=1)
    # c2 = Circle(1, 2, 3, 2)
    # print(f"Circle {c1.id}: {c1.area()} m2")
    # print(c2)

    objects = []
    for i in range(num):
        x, y = np.random.normal(0, 50), np.random.normal(0, 50)
        if np.random.randint(1, 4) == 3:
            geometry_object = Rectangle(x, y, np.random.uniform(3.5, 8.0), np.random.uniform(1.5, 5.0), i)
        else:
            geometry_object = Circle(x, y, np.random.uniform(0.5, 3.0), i)
        objects.append(geometry_object)

    # for o in objects:
    #     print(o)

    return objects


def visualize_objects(objects):
    for o in objects:
        print(o)
        o.visualize()
    plt.gca().set_xlim(-100, 100)
    plt.gca().set_ylim(-100, 100)
    plt.show()


def main():
    objects = generate_objects(20)
    # objects.append(GeometryObject(1, 2, 3))
    visualize_objects(objects)


main()
