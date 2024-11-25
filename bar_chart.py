import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('Electric_Car (1).csv')
df = df['Brand'].value_counts(ascending=True)

fig, ax = plt.subplots(figsize=(10, 10))

# Строим бар-диаграмму
x = np.array(df.index)
y = np.array(df.values)
plt.grid(True,
         linestyle='--',
         color='gray',
         alpha=0.7,
         linewidth=0.5) # пунктирная серая сетка, полупрозрачная
plt.barh(x, y, color='salmon')
plt.title('Количество моделей определенного бренда')
#save to png
plt.savefig('bar_chart.png')
plt.show()
