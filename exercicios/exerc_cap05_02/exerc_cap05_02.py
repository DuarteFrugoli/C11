import numpy as np
import pandas as pd

df_paises = pd.read_csv('paises.csv', sep=';')

# Exerc 1
# Filtrando os países da Oceania
paises_oceania = df_paises.loc[df_paises['Region'].str.contains('Oceania', case=False, na=False), 'Country']

# Exibindo os países da Oceania e a quantidade de países
print(f'Os países da oceania são:\n{paises_oceania}')
print(f'Quantidade de países: {paises_oceania.count()}')

# Exerc 2
# Encontrando o país com a maior população
pais_maior_populacao = df_paises.loc[df_paises['Population'].idxmax()]

# Exibindo o país com a maior população
print(f'O país com a maior população é {pais_maior_populacao['Country'].strip()}, na região {pais_maior_populacao['Region'].strip()}, com a população de {pais_maior_populacao['Population']} pessoas')

# Exerc 3
# Encontrando a taxa de alfabetização média por região
group_region = df_paises.groupby('Region')
media_alfabetizacao = group_region['Literacy (%)'].mean()

# Exibindo a taxa de alfabetização média por região com '%' e 2 casas decimais
media_alfabetizacao_formatada = media_alfabetizacao.apply(lambda x: f'{x:.2f}%')
print(media_alfabetizacao_formatada)

# Exerc 4
paises_sem_costa = df_paises.loc[df_paises['Coastline (coast/area ratio)'] == 0, 'Country']
print(f'Os países sem costa são:\n{paises_sem_costa}')

# Exerc 5
# Criando função para definir nível de mortalidade
def deathrate_urgency(mortalidade):
    if mortalidade < 9:
        return 'Balanced'
    else:
        return 'Urgent'

# Criando campo no dataset com a classificação de urgência, chamado 'Humanitarian Help'
df_paises['Humanitarian Help'] = df_paises['Deathrate'].apply(deathrate_urgency)

# Exibindo o novo dataset
print(df_paises[['Country', 'Deathrate', 'Humanitarian Help']])