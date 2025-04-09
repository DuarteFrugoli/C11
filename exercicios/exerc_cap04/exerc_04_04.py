import numpy as np

np.random.seed()

# Matriz de zeros e uns de tamanho aleatório de 1 a 4
mtz = np.random.randint(0, 2, [np.random.randint(4) + 1, np.random.randint(4) + 1])

# Mostra a Matriz
print(mtz)

# Extrai a quantidade de linhas e colunas
linhas, colunas = mtz.shape

# Quantidade de elementos na matriz
elementos = linhas * colunas

# Diz se o vetor unidimensional seria ímpar ou par
if elementos % 2 == 0:
    print('par')
else:
    print('ímpar')