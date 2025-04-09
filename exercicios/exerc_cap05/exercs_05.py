# Importando numpy e pandas
import numpy as np
import pandas as pd

# Exerc 1
s1 = pd.Series({'Java': 16.25, 'C': 16.04, 'Python': 9.85})
s2 = pd.Series({'C': 16.21, 'Python': 12.12, 'Java': 11.68})

# Exerc 2
print(f'As linguagens de programação representam {s1.sum()}% do total de mercado no ano 1')
print(f'As linguagens de programação representam {s2.sum()}% do total de mercado no ano 2')

# Exerc 3
series_sub = s2.sub(s1)

print(f'A linguagem Java teve a mudança de: {series_sub['Java']:.2f}%')
print(f'A linguagem C teve a mudança de: {series_sub['C']:.2f}%')
print(f'A linguagem Python teve a mudança de: {series_sub['Python']:.2f}%')

# Exerc 4
print(series_sub[series_sub > 0]) # Assim não fica bonito de mostrar, mas provavelmente é isso que a questão quer

# Exerc 5
porcentagem_2anos = s2.add(series_sub.mul(2))
print(porcentagem_2anos.nlargest(1))

# Exerc 6

np.random.seed(10)

# Dataframe
df = pd.DataFrame(
    index=['A', 'B', 'C', 'D', 'E'],
    columns=['W', 'X', 'Y', 'Z'],
    data=np.random.randint(1, 50, [5, 4]))

print(f'A média da coluna X é igual a {df['X'][df['X'] < 30].mean():.2f}')

# Exerc 7
print(f'A média da linha D é igual a {df.loc['D'].mean():.2f}')
print(f'A soma da linha E é igual a {df.iloc[4].sum()}')

# Exerc 8
df_sliced = df.loc[['A', 'C', 'E'], ['X', 'Y']]

print(df_sliced)

print(df_sliced.sum(axis=0))
print(df_sliced.sum(axis=1))