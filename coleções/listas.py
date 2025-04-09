nomes = ['Goku', 'Vegeta', 'Trunks', 'Gohan']

nomes.append('Bulma') # Insere no final
nomes.insert(1, 'kuririn') # Insere em um local específico

print(nomes)

# UPDATE
nomes[0] = 'Goten'

# DELETE
del nomes[1] # Excluindo pelo índice / nomes.pop(1)
nomes.remove('Trunks')

print(nomes)

# nomes.append('Piccolo')

if 'Piccolo' in nomes:
    print('piccolo aqui')
else:
    print('piccolo não está aqui')

# sorted() nomes.sort()