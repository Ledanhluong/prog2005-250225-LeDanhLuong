arr = list(map(int, input("Enter numbers: ").split()))

for num in arr:
    if num > 10:
        print("First number > 10:", num)
        break
