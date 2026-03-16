name = input("Nhập tên: ")

name = name.strip()
words = name.split()

result = ""
for w in words:
    result += w.capitalize() + " "

print("Tên chuẩn hóa:", result.strip())