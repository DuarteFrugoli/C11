import numpy as np

arr = 'Homossexual'

# Retorna -1 para textos em que a substring não aparece
print(np.char.find(arr, 'sexual'))

# Retorna True para cada elemento do array iniciado com uma substring específica
print(np.char.startswith(arr, 'sexual'))

# Maiúsculo e minúsculo
print(np.char.upper(arr))
print(np.char.lower(arr))

# Apenas letras
print(np.char.isalpha(arr))