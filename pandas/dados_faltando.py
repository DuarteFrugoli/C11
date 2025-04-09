import numpy as np
import pandas as pd

dfPaisesv2 = pd.read_csv('paisesv2.csv', sep=';')

# Remove linhas que possuam dados ausentes usando dropna()
dfPaisesv2 = dfPaisesv2.dropna()

# Preenche dados ausentes com um valor padrão usando fillna()
dfPaisesv2 = dfPaisesv2.fillna(0)