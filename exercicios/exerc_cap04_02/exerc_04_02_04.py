import numpy as np

# Carrega o dataset
dataset = np.loadtxt('space.csv', delimiter=';', dtype=str, encoding='utf-8')

# Filtra missões apenas da SpaceX
spacex_mask = dataset[1:, 1] == 'SpaceX'
missoes_spacex = dataset[1:, 4][spacex_mask]
valores_spacex = dataset[1:, 6].astype(float)[spacex_mask]

# Encontra o valor máximo e as missões com esse valor
maior_valor = valores_spacex.max()
missoes_mais_caras = ', '.join(missoes_spacex[valores_spacex == maior_valor])

# Saída
print(f'As missões mais caras da SpaceX foram: {missoes_mais_caras}, custando: {maior_valor}')