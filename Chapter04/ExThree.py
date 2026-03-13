sinh_vien = {
    "Luong": 8,
    "Long": 7,
    "Truc": 9
}

ten = input("Nhập tên sinh viên: ")

if ten in sinh_vien:
    print("Sinh viên tồn tại")
else:
    print("Sinh viên không tồn tại")