n = int(input("Nhap so phan tu: "))

a = []
for i in range(n):
    x = int(input("Nhap phan tu: "))
    a.append(x)

for i in range(n-1):
    for j in range(n-1-i):
        if a[j] < a[j+1]:
            t = a[j]
            a[j] = a[j+1]
            a[j+1] = t
    print("buoc", i+1, ":", a)

print("sau khi sap xep:", a)