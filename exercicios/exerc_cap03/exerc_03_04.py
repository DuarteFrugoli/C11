nomes = []
pesos = []

for i in range(3):
    nomes.append(input(f'Nome da {i+1}ª pessoa: '))
    pesos.append(float(input(f'Peso da {i+1}ª pessoa: ')))

pessoas = {'Nomes':nomes, 'Pesos':pesos}

del nomes
del pesos

print(f'Nome da pessoa mais pesada: {pessoas['Nomes'][pessoas['Pesos'].index(max(pessoas['Pesos']))]}')
print(f'Nome da pessoa mais leve: {pessoas['Nomes'][pessoas['Pesos'].index(min(pessoas['Pesos']))]}')