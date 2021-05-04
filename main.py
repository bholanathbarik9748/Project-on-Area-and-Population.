import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sb

# data initialization
city = pd.read_csv('california_cities.csv')
print(city.head())

# extracting the data we ar interested in
latitude, longitude = city["latd"], city["longd"]
population, area = city["population_total"], city["area_total_km2"]

# to scatter the points, using size and color but without label
sb.set()
plt.scatter(latitude, longitude, label=None, c=np.log10(population), cmap='viridis', s=area, linewidth=0, alpha=0.5)
# plt.axis(aspect='equal')
plt.xlabel('latitude')
plt.ylabel('longitude')
plt.colorbar(label='log$_{10}$(population)')
plt.clim(3, 7)

# now we will crate a legend, we will plot empty lists with the desired size and label
for area in [100, 200, 300]:
    plt.scatter([], [], c='k', alpha=0.3, s=area, label=str(area) + 'km$^2$')
plt.legend(scatterpoints=1, frameon=False, labelspacing=1, title='City Areas')
plt.title("Area and Population of California Cities")
plt.show()