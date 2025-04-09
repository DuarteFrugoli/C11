import numpy as np

# Criando um array unidimensional com 6 elementos
arr = np.arange(6)

# Remodelando o array para uma matriz 3x2 (3 linhas e 2 colunas)
mtz = arr.reshape(3, 2)

print(arr)
print(mtz)

print(mtz.size) # Tamanho do Array
print(mtz.ndim) # Dimensões do Array
print(mtz.shape) # Tupla com o tamanho de cada dimensão do array

# Somando apenas as linhas e apenas as colunas
print(mtz.sum(axis=0)) # Soma os elementos da coluna
print(mtz.sum(axis=1)) # Soma os elementos da linha

# Primeiro elemento da soma das colunas
print(mtz.sum(axis=0)[0])

# Operação entre um vetor e um escalar (Broadcasting)
print(mtz*5) # Todos  os elementos *5
print(mtz/2) # Todos os elementos /2