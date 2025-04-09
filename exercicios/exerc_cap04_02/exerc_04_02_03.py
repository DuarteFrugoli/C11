import numpy as np

# Carrega o dataset
dataset = np.loadtxt('space.csv', delimiter=';', dtype=str, encoding='utf-8')

# Lista das missões removendo espaçoes extras
missoes = np.char.strip(dataset[1:, 2])

# Lista das missões dos EUA
missoes_usa = missoes[np.char.endswith(missoes, 'USA')]

# Saída
print(f'missões realizadas pelos EUA: {missoes_usa.size}')