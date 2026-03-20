from matplotlib import pyplot as plt
label = ["Xuất sắc", "Giỏi", "Trung bình", "Yếu", "Kém"]
values = [6, 10, 12, 4, 1]

plt.bar(label, values)
plt.title("ket qua hoc tap")
plt.xlabel("Xep loai")
plt.ylabel("So hoc sinh")
plt.show()