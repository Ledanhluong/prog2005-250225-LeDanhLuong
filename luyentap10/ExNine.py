class Person:
    def __init__(self, name, age):
        self.name = name
        self.set_age(age)

    def get_name(self):
        return self.name

    def set_age(self, age):
        if age < 0:
            raise ValueError("Tuổi không hợp lệ")
        self.age = age
    def __str__(self):
        return f"Person: {self.name}, {self.age}"

    def say_hello(self):
        print("Xin chào, tôi là", self.name)

    @classmethod
    def loai(cls):
        return "Đây là class Person"

    @staticmethod
    def thong_tin():
        return "Static method trong Person"
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age
class Student(Person):
    def __init__(self, name, age, score):
        super().__init__(name, age)
        self.set_score(score)
    def set_score(self, score):
        if score < 0 or score > 10:
            raise ValueError("Điểm không hợp lệ")
        self.score = score

    def __str__(self):
        return f"Student: {self.name}, {self.age}, {self.score}"

    def study(self):
        print(self.name, "đang học")
p1 = Person("Luong", 19)
p2 = Person("Luong", 19)
print(p1)
p1.say_hello()
print(Person.loai())
print(Person.thong_tin())

print("So sánh p1 và p2:", p1 == p2)

s1 = Student("Long", 18, 8)
print(s1)
s1.study()