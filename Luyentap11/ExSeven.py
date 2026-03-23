import csv
ten = input("Ten: ")
tuoi = input("tuoi: ")
id = input("ID: ")
f = open("nhanvien.txt", "w", encoding="utf-8")
f.write("ten: " + ten + "\n")
f.write("tuoi: " + tuoi + "\n")
f.write("ID: " + id)
f.close()
with open("nhanvien.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["ten", "tuoi", "ID"])
    writer.writerow([ten, tuoi, id])
print("da luu file")