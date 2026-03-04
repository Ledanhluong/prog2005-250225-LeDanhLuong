arr = list(map(int, input("Enter numbers: ").split()))

m = int(input("nhap so hang: "))
n = int(input("nhap so cot: "))

A = []
B = []
C = []

print("nhap ma tran A:")
for i in range(m):
    row = list(map(int, input().split()))
    A.append(row)

print("nhap ma tran B:")
for i in range(m):
    row = list(map(int, input().split()))
    B.append(row)

for i in range(m):
    row = []
    for j in range(n):
        row.append(A[i][j] + B[i][j])
    C.append(row)

print("tra ket qua ma tran:")
for row in C:
    print(row)
max_value = arr[0]
min_value = arr[0]

for num in arr:
    if num > max_value:
        max_value = num
    if num < min_value:
        min_value = num

print("Max:", max_value)
print("Min:", min_value)
