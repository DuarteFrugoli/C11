while True:
    num = int(input('digite um número entre 1000 e 9999: '))

    if 1000 <= num <= 9999:
        break

    print('para de zoar  bagui')

m = num // 1000
c = (num // 100) % 10
d = (num // 10) % 10
u = num % 10

print(f'unidade: {u}')
print(f'dezena: {d}')
print(f'centena: {c}')
print(f'milhar: {m}')