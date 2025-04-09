import numpy as np

# Carregando o dataset
dataset = np.loadtxt('paises.csv', delimiter=';', dtype=str, encoding='utf-8')

# Saída da parte necessária do dataset
print(dataset[1:, 0:4])