a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
c = float(input("Nhap c: "))

print("So lon nhat:", max(a, b, c))
print("So nho nhat:", min(a, b, c))

if a == 0:
    if b == 0:
        if c == 0:
            print("Vo so nghiem")
        else:
            print("Vo nghiem")
    else:
        print("x =", -c / b)
else:
    d = b * b - 4 * a * c

    if d < 0:
        print("Vo nghiem")
    elif d == 0:
        print("x =", -b / (2 * a))
    else:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        print("x1 =", x1)
        print("x2 =", x2)