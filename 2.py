print("in ra theo thứ tự giảm dần")
for i in range(111, 16, -1):
    if i % 2 != 0:
        print(i)
print("in ra số nguyên tố")
for i in range(16, 111):
    la_nguyen_to = True

    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            la_nguyen_to = False
            break

    if la_nguyen_to:
        print(i)