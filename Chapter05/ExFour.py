import pandas as pd
import matplotlib.pyplot as plt

cities = pd.read_csv('california_cities.csv')
top_area = cities.sort_values(by='area_total_km2', ascending=False).head(10)
plt.figure(figsize=(10, 6))
plt.barh(top_area['city'], top_area['area_total_km2'])
plt.xlabel('Diện tích (km2)')
plt.title('Top 10 thành phố lớn nhất California theo diện tích')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()