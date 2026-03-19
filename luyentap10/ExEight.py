ds = []
for i in range(5):
    s = input("Nhập chuỗi thứ " + str(i + 1) + ": ")
    ds.append(s)
n = len(ds)
for i in range(n):
    for j in range(0, n - i - 1):
        if len(ds[j]) < len(ds[j + 1]):
            temp = ds[j]
            ds[j] = ds[j + 1]
            ds[j + 1] = temp

        print("Bước:", ds)

print("Kết quả:", ds)