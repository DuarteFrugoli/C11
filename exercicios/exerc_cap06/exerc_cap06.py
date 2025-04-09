import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Importando datasets
df_paises = pd.read_csv('paises.csv', sep=';')
df_space = pd.read_csv('space.csv', sep=';')

# Mostrando as colunas de df_paises
print(df_paises.columns)

# Exerc 1
# Filtrando os dados para os países da América do Norte
df_norte = df_paises[df_paises['Region'] == 'América do Norte']
df_norte = df_norte[['Country', 'Deathrate', 'Birthrate']]
df_norte = df_norte.set_index('Country')
df_norte = df_norte.transpose()
df_norte.plot(kind='line', figsize=(10, 5))
plt.title('Taxa de Mortalidade e Natalidade dos Países da América do Norte')
plt.xlabel('Taxa')
plt.ylabel('Países')
plt.legend(title='Países')
plt.grid()
plt.show()

# Exerc 2


# Exerc 3
