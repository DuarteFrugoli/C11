import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df_space = pd.read_csv('space.csv', sep=';')

# Filtra os dados para os EUA e China e remove duplicatas
empresas_eua = df_space[df_space["Location"].str.contains("USA")]["Company Name"].drop_duplicates()
empresas_china = df_space[df_space["Location"].str.contains("China")]["Company Name"].drop_duplicates()

# Conta o número de empresas únicas
num_empresas = {
    "EUA": len(empresas_eua),
    "China": len(empresas_china)
}

# Cria o gráfico de barras
plt.figure(figsize=(8, 5))
plt.bar(num_empresas.keys(), num_empresas.values(), color=['blue', 'red'])

# Títulos e legendas
plt.title("Número de Empresas Espaciais - EUA vs China")
plt.xlabel("País")
plt.ylabel("Número de Empresas")
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Exibe o gráfico
plt.tight_layout()
plt.show()