import numpy as np

# Carregando o dataset
dataset = np.loadtxt('paises.csv', delimiter=';', dtype=str, encoding='utf-8')

# Regiões do dataset e um texto com cada um para melhorar a saída
regioes = np.char.strip(np.unique(dataset[1:, 1]))
texto_regioes = ', '.join(regioes)

# Saída
print(f'No dataset existem {regioes.size} regiões, sendo elas: {texto_regioes}.')