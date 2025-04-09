import numpy as np

# Carrega o dataset
dataset = np.loadtxt('space.csv', delimiter=';', dtype=str, encoding='utf-8')

# Faz o cálculo de quantidade de sucessos em porcentagem
porcentagem_sucesso = np.mean(dataset[1:, 7] == 'Success') * 100

# Saída
print(f'Porcentagem de missões que deram certo: {porcentagem_sucesso:.2f}%')