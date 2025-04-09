import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df_paises = pd.read_csv('paises.csv', delimiter=';')

# top 5 países com maior pip per capita
df_top5 = df_paises.nlargest(5, 'GDP ($ per capita)')

# gráfico de barras
eixo_x = df_top5['Country']
eixo_y = df_top5['GDP ($ per capita)']

plt.bar(eixo_x, eixo_y, color='blue')

plt.show()