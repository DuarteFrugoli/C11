import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Importando dataset
df_paises = pd.read_csv('paises.csv', sep=';')

# Limpando espaços em branco nas colunas relevantes
df_paises["Region"] = df_paises["Region"].str.strip()
df_paises["Country"] = df_paises["Country"].str.strip()

# Convertendo as colunas de taxas para float
df_paises["Deathrate"] = pd.to_numeric(df_paises["Deathrate"], errors='coerce')
df_paises["Birthrate"] = pd.to_numeric(df_paises["Birthrate"], errors='coerce')

# Filtra apenas os países da América do Norte
america_norte = df_paises[df_paises["Region"] == "NORTHERN AMERICA"]

# Remove linhas com valores ausentes
america_norte = america_norte.dropna(subset=["Deathrate", "Birthrate"])

# Ordena pelo nome do país para manter o gráfico organizado
america_norte = america_norte.sort_values("Country")

# Define os países como eixo X
paises = america_norte["Country"]

# Plota os dados
plt.figure(figsize=(12, 6))
plt.plot(paises, america_norte["Deathrate"], label="Taxa de Mortalidade (Deathrate)", marker='o')
plt.plot(paises, america_norte["Birthrate"], label="Taxa de Natalidade (Birthrate)", marker='s')

# Títulos e legendas
plt.title("Taxa de Mortalidade e Natalidade - América do Norte")
plt.xlabel("Países")
plt.ylabel("Taxa")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()

# Exibe o gráfico
plt.show()

print(america_norte[["Country", "Birthrate", "Deathrate"]])