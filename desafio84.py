pessoa = []
grupo = []
total = 0
gordos = []
magros = []

while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(int(input('Peso: ')))
    grupo.append(pessoa[:])
    pessoa.clear()

    r = str(input('Deseja continuar?: [S/N]'))
    if r not in 'Ss':
        break
for p in grupo:
    total+=1
    if p[1] >= 100:
        gordos.append(p[0])
    else:
        magros.append(p[0])

print(f'Foram cadastradas {total} pessoas')
print(f'As pessoas de nome {gordos} são gordas (acima de 100kg)')
print(f'As pessoas de nome {magros} são magras')
