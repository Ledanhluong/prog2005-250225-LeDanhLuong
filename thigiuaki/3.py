n = int(input("Nhap n: "))

print("tam giac 1")
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end="")
    print()

print("Tam giac 2:")
for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end="")
    for j in range(2*i-1):
        print("*", end="")
    print()