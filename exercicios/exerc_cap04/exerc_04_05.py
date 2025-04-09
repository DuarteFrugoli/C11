import numpy as np

# Seed 10
np.random.seed(10)

# Cria a matriz aleatória 4x4
mtz = np.random.randint(1, 51, [4, 4])

# Mostra a matriz
print(mtz)

# Extrai a quantidade de linhas e colunas
medias_linhas = mtz.mean(axis=1)
medias_colunas = mtz.mean(axis=0)

# Mostra a média de todas as linhas e todas as colunas
for _i in range(4):
    print('linha {}, média = {}'.format(_i, medias_linhas[_i]))
for _i in range(4):
    print('coluna {}, média = {}'.format(_i, medias_colunas[_i]))

# Mostra a maior média das linhas e a maior médias das colunas
print(f'maior média das linhas: {medias_linhas.max()}')
print(f'maior média das colunas: {medias_colunas.max()}')

# Matriz com elementos únicos e suas quantidades
mtz_unique = np.unique(mtz, return_counts = True)

# Mostra os elementos únicos e suas quantidades
for _i in range(mtz_unique[0].size):
    print('O elemento \"{}\" aparece {} vezes'.format(mtz_unique[0][_i], mtz_unique[1][_i]))

# Mostra apenas os elementos que se repetem 2x
print('Os elementos que aparecem 2x são:')
for _i in range(mtz_unique[0].size):
    if mtz_unique[1][_i] == 2:
        print(mtz_unique[0][_i])