import numpy as np

# Carregando o dataset
dataset = np.loadtxt('paises.csv', delimiter=';', dtype=str, encoding='utf-8')

# Máscara dos paises pertecentes a América Latina e Caribe
america_latina_caribe_mask = np.char.startswith(dataset[1:, 1], 'LATIN AMER. & CARIB')

# Renda per capita e nome de cada país
rpc_america_latina_caribe = dataset[1:, 8][america_latina_caribe_mask].astype(float)
paises_rpc_america_latina_caribe = dataset[1:, 0][america_latina_caribe_mask]

# Saída do nome do país com maior rpc
print(f'O país com maior renda per capita da américa latina e caribe é o {paises_rpc_america_latina_caribe[rpc_america_latina_caribe.argmax()]}')