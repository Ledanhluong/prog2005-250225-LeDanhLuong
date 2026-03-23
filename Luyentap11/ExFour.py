a = [1, 3, 5]
x = int(input("Nhap so them: "))
a.append(x)
k = int(input("Nhap k: "))
dem = 0
for i in a:
    if i == k:
        dem += 1
print("So lan xuat hien:", dem)
def la_snt(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

tong = 0
for i in a:
    if la_snt(i):
        tong += i

print("Tong so nguyen to:", tong)
a.sort()
print("Danh sach sap xep", a)
a.clear()
print("Danh sach xoa:", a)