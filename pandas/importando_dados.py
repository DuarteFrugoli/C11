import numpy as np
import pandas as pd

# Importando dados do csv de paises
dfPaises = pd.read_csv('paises.csv', delimiter=';')
dfPaisesv2 = pd.read_csv('paisesv2.csv', delimiter=';')

print(dfPaises)

# Colunas
print(dfPaises.columns)

# Acessando os primeiros n registros
print(dfPaises.head(3))

# Acessando os últimos n registros
print(dfPaises.tail(3))

# Verifica quanto % uma população representa no mundo

# População mundial
total_population = np.sum(dfPaises['Population'])

# Broadcasting para calcular a %  da população de cada país
seriesPercPopulation = (dfPaises['Population']/total_population)*100

# Adicionando nova coluna no dataset com essa informação
dfPaises['% Population'] = np.round(seriesPercPopulation, 3)

# Salvando um novo arquivo com essa atualiazação
dfPaises.to_csv('paisesv2.csv', sep=';')

# Pegando os seis países mais populosos do planeta
print(dfPaisesv2.nlargest(6, '% Population'))

# dfPaises.drop('Region', axis=1) para excluir (exemplo)
# axis=1 exclui colunas, axis=0 exclui linhas

# Agrupando países por região e mostrando quantidades de cada região
group_region = dfPaises.groupby('Region')
print(group_region.count()['Country'])

# Soma da população de cada região
print(group_region.sum()['Population'])

# Descrevendo estatísticas importantes
print(group_region.describe())