import numpy as np
import pandas as pd

dfPaisesv2 = pd.read_csv('paisesv2.csv', sep=';')

def tenpercent(x):
    return x*0.9

# Mortalidade dos países
death_rate1 = dfPaisesv2['Deathrate']

# Aplicando método com apply()
# Diminuindo a mortalidade em 10%
death_rate2 = dfPaisesv2['Deathrate'].apply(tenpercent)

# Concatenando e mostrando as duas Series
print(pd.concat([death_rate1, death_rate2], axis=1))