class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print("Gâu Gâu")


dog1 = Dog("Thành")

print("Tên:", dog1.name)
dog1.sound()