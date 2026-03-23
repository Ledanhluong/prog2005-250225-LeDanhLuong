a = ['aaaaaaaa', 'fdfdf', 'helo', 'yu', 'e']
x = input("Nhap chuoi can tim: ")
left = 0
right = len(a) - 1
tim = False
while left <= right:
    mid = (left + right) // 2
    if a[mid] == x:
        print("Da tim thay tai vi tri:", mid+1)
        tim = True
        break
    elif len(a[mid]) < len(x):
        right = mid - 1
    else:
        left = mid + 1
if tim == False:
    print("Khong tim duoc")