while True:
    dist = float(input('distância da viagem: '))
    
    if dist > 0:
        break

    print('não te daremos dinheiro')

if dist > 200:
    preco = 0.45
else:
    preco = 0.50

print(f'o preço da viagem será de {round(dist*preco, 2)} reais')