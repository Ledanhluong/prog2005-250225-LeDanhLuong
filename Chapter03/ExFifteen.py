#Dùng slicing
s = input("Enter string: ")
print("Reversed:", s[::-1])
#Không dùng slicing
s = input("Enter string: ")
reversed_s = ""

for ch in s:
    reversed_s = ch + reversed_s

print("Reversed:", reversed_s)
