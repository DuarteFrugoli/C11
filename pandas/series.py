import numpy as np

# Importando o pandas
import pandas as pd

# Coleção de labels
labels = ['a', 'b', 'c']

# Coleção de dados
dados = [10, 20, 30]

# Series
s = pd.Series(index=labels, data=dados)

# Parece um dicionário

print(s['b'])

s1 = pd.Series({'a': 10, 'b': 20, 'c': 30, 'd': 10})
s2 = pd.Series({'a': 10, 'b': 50, 'c': 80})

# Printa a soma dos pares
print(s1 + s2)

# Printa a soma inclusive dos que não tem pares com um valor especificado
print(s1.add(s2, fill_value=0))

print(np.mean(s1)) # Compatibilidade com o numpy

# Filtrando só o necessário
print(s1[['a', 'c']])

# Slicing nas Series com índices numéricos
print(s1[1:])

# Condicionais para Series
print(s1[s1 > 25])
print(s1[s1 > s1.mean()])
print(s1[s1/2 == 10])