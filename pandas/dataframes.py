import numpy as np
import pandas as pd

np.random.seed(10)

# Dataframe
df = pd.DataFrame(
    index=['A', 'B', 'C', 'D', 'E'],
    columns=['W', 'X', 'Y', 'Z'],
    data=np.random.randint(1, 50, [5, 4]))

# Parabéns agora você está usando o Excel

# Cada coluna é uma Series
print(df['W'])

# Acessando múltiplas Series
print(df[['W', 'Z']])

# Valor específico
print(df['W']['A'])

# Slicing com loc()
print(df.loc[['A', 'B'], ['X', 'Y', 'Z']])

# Slicing com iloc()
print(df.iloc[0:2, 1:])