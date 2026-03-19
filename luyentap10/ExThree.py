while True:
    def giai_thua(n):
        if n == 0 or n == 1:
            return 1
        return n * giai_thua(n - 1)
    n = int(input("nhap so: " ))
    print("giai thua: ", giai_thua(n))