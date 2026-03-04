arr = list(map(int, input("Enter numbers: ").split()))

total = 0

print("Even numbers:")
for num in arr:
    if num % 2 == 0:
        print(num)
        total += num

print("Sum of even numbers:", total)
