import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df_paises = pd.read_csv('paises.csv', delimiter=';')

# Países sem costa marítima
df_paises_sem_costa = df_paises[df_paises['Coastline (coast/area ratio)'] == 0]

# Extraindo a quantidade de países sem costa marítima
qt_paises_sem_costa = len(df_paises_sem_costa)

# Extraindo a quantidade de países com costa marítima
qt_paises_com_costa = len(df_paises) - qt_paises_sem_costa

# Criando os dados para o gráfico de pizza
plt.pie([qt_paises_sem_costa, qt_paises_com_costa], labels=['% Sem Costa', 'Com Costa'], autopct='%1.1f%%', startangle=90, colors=['red', 'blue'])

plt.show()