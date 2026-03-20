from matplotlib import pyplot as plt

categories = ['Sản phẩn A', 'Sản phẩm B', 'Sản phẩm C', 'Sản phẩm D', 'Sản Phẩm E']
values = [30, 25, 15, 20, 10]


plt.pie(values, labels=categories, autopct="%1.1f%%")
plt.title("Phần trăm doanh số")
plt.show()