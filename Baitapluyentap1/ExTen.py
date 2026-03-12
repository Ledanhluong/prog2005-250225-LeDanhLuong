while True:
    filename = "products.txt"

    code = input("Nhập mã sản phẩm: ")
    name = input("Nhập tên sản phẩm: ")
    price = float(input("Nhập giá: "))

    file = open(filename, "a", encoding="utf-8")
    file.write(code + ";" + name + ";" + str(price) + "\n")
    file.close()

    products = []

    file = open(filename, "r", encoding="utf-8")

    for line in file:
        data = line.strip().split(";")
        code = data[0]
        name = data[1]
        price = float(data[2])

        products.append([code, name, price])

    file.close()

    products.sort(key=lambda x: x[2], reverse=True)

    for p in products:
        print(p)