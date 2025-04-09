nome = input('digite seu nome: ')

print(f'nome maiúsculo: {nome.upper()}')
print(f'nome minúsculo: {nome.lower()}')
print(f'seu nome tem {len(nome.replace(' ', ''))} letras')

partes = nome.split()

if len(partes) > 1:
    partes[-1] = 'do inatel'
    nome = ' '.join(partes)
else:
    nome = nome + ' do inatel'

print(f'Você é o {nome}')