arr = list(map(int, input("Enter numbers: ").split()))

print("Odd numbers:")
for num in arr:
    if num % 2 != 0:
        print(num)
