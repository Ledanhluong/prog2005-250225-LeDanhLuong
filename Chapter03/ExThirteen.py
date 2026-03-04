s = input("nhap 1 chuoi: ")
s = s.lower()

if s == s[::-1]:
    print("tu dao nguoc")
else:
    print("khong phai tu dao nguoc")
