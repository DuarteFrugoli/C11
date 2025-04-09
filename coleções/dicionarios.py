# Dicionários são coleções MUTÁVEIS com ÍNDICES PERSONALIZADOS
pessoa = {'nome':'Goku', 'idade':42}

print(pessoa)
# Acessar
print(pessoa['nome'])
# Insert
pessoa['sexo'] = 'H'
# Update
pessoa['nome'] = 'Vegeta'
# Delete
del pessoa['idade']

print(pessoa)