m = int(input("nhap so hang: "))
n = int(input("nhap so cot: "))
a = []
b = []
print("Nhap ma tran A:")
for i in range(m):
    row = list(map(int, input().split()))
    if len(row) != n:
        print("loi nhap")
        exit()
    a.append(row)
print("nhap ma tran B:")
for i in range(m):
    row = list(map(int, input().split()))
    if len(row) != n:
        print("loi nhap")
        exit()
    b.append(row)
c = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(a[i][j] + b[i][j])
    c.append(row)
print("Ma tran tong:")
for i in c:
    print(i)