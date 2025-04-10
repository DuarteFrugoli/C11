import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Importando dataset
df_space = pd.read_csv('space.csv', sep=';')

# Filtra os dados para a empresa Roscosmos
roscosmos_missoes = df_space[df_space["Company Name"] == "Roscosmos"]

# Conta o número de missões bem-sucedidas e mal-sucedidas
status_missoes = roscosmos_missoes["Status Mission"].value_counts()

# Cria o gráfico de torta
plt.figure(figsize=(8, 8))
plt.pie(status_missoes, labels=status_missoes.index, autopct='%1.1f%%', startangle=90, colors=['green', 'red'])

# Títulos
plt.title("Porcentagem de Sucesso e Falha das Missões da Roscosmos")

# Exibe o gráfico
plt.tight_layout()
plt.show()