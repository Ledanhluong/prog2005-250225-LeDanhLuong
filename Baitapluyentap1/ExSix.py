s = input("Nhập chuỗi số: ")

numbers = s.split(";")

nums = []
for i in numbers:
    nums.append(int(i.strip()))

for n in nums:
    print(n)

even = 0
for n in nums:
    if n % 2 == 0:
        even += 1

print("Số chẵn:", even)

neg = 0
for n in nums:
    if n < 0:
        neg += 1

print("Số âm:", neg)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

prime = 0
for n in nums:
    if is_prime(n):
        prime += 1

print("Số nguyên tố:", prime)

avg = sum(nums)/len(nums)

print("Trung bình:", avg)