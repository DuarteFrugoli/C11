futebolistas = ['Barcelona', 'Real Madrid', 'AC Milan', 'Manchester City', 'Liverpool']

print(f'3 primeiros colocados: {futebolistas[:3]}')
print(f'2 últimos colocados: {futebolistas[-2:]}')
print(f'Times em ordem alfabética: {sorted(futebolistas)}')
print(f'Posição do Barça: {futebolistas.index('Barcelona')+1}º lugar')