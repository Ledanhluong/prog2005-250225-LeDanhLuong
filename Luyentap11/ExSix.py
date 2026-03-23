d = {}

n = int(input("nhap so nguoi: "))

for i in range(n):
    ten = input("Ten: ")
    tuoi = int(input("tuoi: "))
    d[ten] = tuoi
tong = 0
for i in d:
    tong += d[i]
print("tuoi trung binh:", tong / n)
items = list(d.items())
for i in range(len(items)):
    max_idx = i
    for j in range(i + 1, len(items)):
        if items[j][1] > items[max_idx][1]:
            max_idx = j
    items[i], items[max_idx] = items[max_idx], items[i]
print("sap xep:")
for i in items:
    print(i[0], ":", i[1])