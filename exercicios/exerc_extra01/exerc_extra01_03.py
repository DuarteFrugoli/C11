import numpy as np

# Carregando o dataset
dataset = np.loadtxt('paises.csv', delimiter=';', dtype=str, encoding='utf-8')

# Média de alfabetização de todos os países
media_alfabetizacao = np.mean(dataset[1:, 9].astype(float))

# Saída em porcentagem com 2 casas decimais de precisão
print(f'A média de alfabetização mundial é de {media_alfabetizacao:.2f}%')