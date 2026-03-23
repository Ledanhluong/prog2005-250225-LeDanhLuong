while True:
    nums = list(map(int, input("Nhap so: ").split()))

    tong = 0

    print("So chan:")
    for i in nums:
        if i % 2 == 0:
            print(i, end=" ")
            tong += i

    print("\nTong:", tong)