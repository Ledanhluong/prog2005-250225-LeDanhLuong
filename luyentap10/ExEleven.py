while True:
    print("\n--- MENU ---")
    print("1. Đao chuoi")
    print("2. Nhap mat khau")
    print("0. Thoat")

    chon = input("Chon: ")

    if chon == "1":
        s = input("Nhap chuoi: ")
        dao = ""
        for i in range(len(s)-1, -1, -1):
            dao += s[i]
        print("Ket qua:", dao)

    elif chon == "2":
        mk = ""
        while mk != "python123":
            mk = input("Nhap mat khau: ")
        print("DUNG!")

    elif chon == "0":
        break

    else:
        print("Chọn sai!")