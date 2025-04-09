import numpy as np

# Semente aleatória para máquinas diferentes terem os mesmos resultados
np.random.seed(0)

# Retorna uma lista com números inteiros aleatórios entre 0 a 5 com 10 elementos
print(np.random.randint(0, 5, 10))

# Mesma coisa para um array bidimensional
print(np.random.randint(0, 5, [4,4]))

mtz = np.array([[0, 1, 0], [2, 0, 0], [0, 0, 3]])

# Retorna elementos únicos independente da dimensão
print(np.unique(mtz))

# Retorna a frequência de cada elemento único
print(np.unique(mtz, return_counts=True))