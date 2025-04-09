import numpy as np

# Preenchendo as arrays
arr = np.ones(8) # Uns
arr2 = np.random.randint(0, 10, 8) # Aleatório entre 0 a 9
arr3 = (arr + arr2) # Soma das arrays 1 e 2

# Saída para conferir
print('array 1:', arr)
print('array 2:', arr2)
print('soma dos arrays (array 3):', arr3)

# Soma de todos os termos da array 3
print('Soma dos elementos do array 3:', arr3.sum())

# Se a soma for maior ou igual 40 mais linhas, senão mais colunas
if arr3.sum() >= 40:
    mtz = arr3.reshape(4, 2)
else:
    mtz = arr3.reshape(2, 4)

# Mostra a nova array depois do reshape
print('Array após reshape:\n', mtz)