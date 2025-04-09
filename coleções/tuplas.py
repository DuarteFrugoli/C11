nomes = ('Goku', 'Vegeta', 'Trunks', 'Gohan')

print(nomes)
# SLICING DE DADOS
print(nomes[0]) # Goku
# No Python, o primeiro índice de uma coleção é INCLUSIVE e o segundo EXCLUSIVE
print(nomes[:2]) # Goku e Vegeta
print(nomes[2:]) # Trunks e Gohan
print(nomes[1:3]) # Vegeta e Trunks
print(nomes[-1]) # Gohan
print(nomes[-2]) # Trunks
# Tuplas são imutáveis
# nomes[0] = 'Bulma' # não funciona

for nome in nomes:
    print(nome)

# Tuplas aceitam elementos de tipos diferentes

print(sorted(nomes)) # Ordem alfabética