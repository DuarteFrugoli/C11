import numpy as np

# Carregando o dataset
dataset = np.loadtxt('paises.csv', delimiter=';', dtype=str, encoding='utf-8')

# Máscara de países da América do Norte
america_do_norte_mask = np.char.startswith(dataset[1:, 1], 'NORTHERN AMERICA')

# Saída de quantos países pertencem a América do Norte
print(f'A América do Norte possui {np.sum(america_do_norte_mask)} países')