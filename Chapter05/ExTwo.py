from matplotlib import pyplot as plt
import numpy as np

x = np.arange(-5, 5, 0.1)
y = x**2
z = x**3
plt.figure(figsize=(5, 4))
plt.plot(x, y, 'b', label="y = x^2")
plt.plot(x, z, 'r', label="y = x^3")
plt.title("Đồ thị y = x^2 và y = x^3")
plt.legend()
plt.show()