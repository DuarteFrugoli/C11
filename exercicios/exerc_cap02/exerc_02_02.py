num = int(input('número para fazer a tabuada: '))
i = int(input('tabuada até: '))

for _i in range(1, i+1):
    print('{} * {} = {}'.format(num, _i, num*_i))