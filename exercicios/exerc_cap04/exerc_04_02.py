import numpy as np

arr = np.arange(0, 52, 2) # Array pares de 0 a 51
arr2 = np.arange(100, 49, -2) # Array pares de 100 a 50

# No exercício fala para pegar os pares de 100 a 50, então o 50 vai repetir (acho que esse não era o intuito)

# Mostrando o arrays
print('Array 1:', arr)
print('Array 2:', arr2)

# Concatenando e mostrando em ordem crescente (50 repete)
print('Array concatenada:', np.sort(np.concatenate([arr, arr2])))