colors = ["Red", "Blue", "Green", "Yellow", "Black"]

try:
    colors.remove("Green")
except:
    print("Green not found in list")

print("Final list:", colors)
