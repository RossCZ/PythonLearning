# instance method: works only on the instance of the class
# class method: works with class attributes
# static method: works only with passed parameters
# property

class Fox:
    class_attr_name = "Vulpes vulpes"

    def __init__(self, name, weight):
        self.instance_attr_name = name
        self.instance_attr_weight = weight

    @property
    def weight_lbs(self):
        return self.instance_attr_weight * 2.20462

    def introduce(self):
        print(f"Fox named {self.instance_attr_name}")

    @classmethod
    def about(cls):
        print(f"Latin name: {cls.class_attr_name}")

    @staticmethod
    def show_info(static_method_param):
        print(f"{static_method_param} forest animals")


fox = Fox("Ben", 5)
fox.introduce()
Fox.about()
Fox.show_info("Black")
print(fox.weight_lbs)
