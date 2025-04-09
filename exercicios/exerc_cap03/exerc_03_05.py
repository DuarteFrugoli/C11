nomes = []
idades = []
sexo = []

n = int(input('Quantas pessoas deseja analisar: '))

for i in range(n):
    nomes.append(input(f'Nome da {i+1}ª pessoa: '))
    idades.append(int(input(f'Idade da {i+1}ª pessoa: ')))
    sexo.append(input(f'Sexo da {i+1}ª pessoa (H - homi / M - muié): ').upper())

pessoas = {'Nomes':nomes, 'Idades':idades, 'Sexo':sexo}

del nomes
del idades
del sexo

media = 0
msub20 = 0

for i in range(n):
    media += pessoas['Idades'][i]
    
    if pessoas['Sexo'][i] == 'M' and pessoas['Idades'][i] < 20:
        msub20 += 1

media = media / n

print(f'Média das idades: {media}')
print(f'Quantidade de mulheres com menos de 20 anos: {msub20}')