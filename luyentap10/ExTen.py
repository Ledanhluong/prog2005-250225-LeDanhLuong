ds = []

for i in range(5):
    s = input("Nhap chuoi: ")
    ds.append(s)

n = len(ds)

for i in range(n):
    for j in range(n - 1):
        if len(ds[j]) < len(ds[j+1]):
            temp = ds[j]
            ds[j] = ds[j+1]
            ds[j+1] = temp

        print("Buoc:", ds)

print("Ket qua:", ds)