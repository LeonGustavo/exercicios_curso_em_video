pessoas = []
pessoa = {}
mulheres = []
acima = []
c = 0
idade = 0
while True:
    c = c + 1
    pessoa['nome'] = str(input('Digite o nome: ')).strip().upper()
    pessoa['sexo'] = str(input('Digite o sexo [M/F]: ')).strip().upper()
    while pessoa['sexo'] not in 'MmFf':
        pessoa['sexo'] = str(input('Digite o sexo [M/F]: ')).strip().upper()
    if pessoa['sexo'] in 'Ff':
        mulheres.append(pessoa['nome'])
    pessoa['idade'] = int(input('Digite a idade: '))
    idade = idade + pessoa['idade']
    pessoas.append(pessoa.copy())
    pessoa.clear()
    op = str(input('Deseja continuar [S/N]? ')).strip().upper()
    while op not in 'SsNn':
        op = str(input('Deseja continuar [S/N]? ')).strip().upper()
    if op in 'Nn':
        break
    if op not in 'NnSs':
        op = str(input('Deseja continuar [S/N]? ')).strip().upper()
idade = idade / c
for i in range(0, len(pessoas)):
    if pessoas[i]['idade'] > idade:
        acima.append(pessoas[i])
print('-=-'*30)
print(f'Foram cadastradas {c} pessoas!!!')
print(f'A média de idade entre elas é: {idade}')
print('As mulheres do grupo são: ', end=' ')
for i in range(0, len(mulheres)):
    print(f'{mulheres[i]}', end=' ')
print()
print('As pessoas com idade acima da média do grupo são: ')
for i in range(0, len(acima)):
    print(f'{acima[i]["nome"]}')
print('-=-'*30)
print('>>>>> A lista completa <<<<<')
for k, v in enumerate(pessoas):
    print(f'{k+1}º == {v}')
print('-=-'*30)


