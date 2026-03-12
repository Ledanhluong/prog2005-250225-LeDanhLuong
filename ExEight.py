class Student:
    def __init__(self, name, score):
        self.name = name

        if 0 <= score <= 10:
            self.score = score
        else:
            self.score = 0
            print("Điểm không hợp lệ")

s1 = Student("Khánh", 8)
print(s1.name, s1.score)

s2 = Student("Bình", 10)
print(s2.name, s2.score)

s3 = Student("Lượng", -2)
print(s3.name, s3.score)