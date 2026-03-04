arr = list(map(int, input("Enter numbers: ").split()))
x = int(input("Enter number to find: "))

found = -1

for i in range(len(arr)):
    if arr[i] == x:
        found = i
        break

print("Index:", found)
