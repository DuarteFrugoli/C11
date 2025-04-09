aluno = {'Nome':'', 'Média':0, 'Situação': ''}

nome = input('Digite seu nome: ')
media = float(input('digite sua média: '))

aluno['Nome'] = nome
aluno['Média'] = media

if aluno['Média'] >= 50:
    aluno['Situação'] = 'AP'
else:
    aluno['Situação'] = 'RP'

print(aluno)