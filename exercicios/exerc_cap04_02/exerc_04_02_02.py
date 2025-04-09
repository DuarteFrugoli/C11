import numpy as np

# Carrega o dataset
dataset = np.loadtxt('space.csv', delimiter=';', dtype=str, encoding='utf-8')

# Lista apenas com os valores das missões
lista_valores = dataset[1:, 6].astype(float)

# Valores maiores que 0
lista_valores = lista_valores[lista_valores > 0]

# Media dos valores
media = np.mean(lista_valores)

# Saída
print(f'Custo médio: {media:.2f}')