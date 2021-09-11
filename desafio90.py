aluno = {}

aluno['nome'] = str(input('Qual o nome do aluno?'))
aluno['media'] = float(input('Qual é a média do Aluno?'))

if aluno['media'] >= 6:
    aluno['situacao'] = 'top'
else:
    aluno['situacao'] = 'um cocozao'

for k,v in aluno.items():
    print(f'{k} é igual a {v}')