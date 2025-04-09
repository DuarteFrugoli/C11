import numpy as np

# Carrega o dataset
dataset = np.loadtxt('space.csv', delimiter=';', dtype=str, encoding='utf-8')

# Pega os nomes das empresas e as quantidades de missões
empresa, quantidade = np.unique(dataset[1:, 1], return_counts=True)

# Itera empresas e quantidades exibindo para o usuário
for emp, qtd in zip(empresa, quantidade):
    print(f'A empresa "{emp}" realizou {qtd} missões.')