alunos = [{'Nome':'Xi Jinping',     'Média':32,     'Situação':''},
         {'Nome':'Elon Musk',       'Média':77,     'Situação':''},
         {'Nome':'Renzo Mesquita',  'Média':100,    'Situação':''},
         {'Nome':'Felipe Neto',     'Média':3,      'Situação':''}]

for aluno in alunos:
    if aluno['Média'] >= 50:
        aluno['Situação'] = 'AP'
    else:
        aluno['Situação'] = 'RP'
    
    print(aluno)

# Eu não li direito o exercício e fiz essa cagada aí