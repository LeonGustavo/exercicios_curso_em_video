ficha = list()

while True:
    nome = str(input('Digite um nome '))
    nota1 = float(input('Digite a nota 1 '))
    nota2 = float(input('Digite a nota 2 '))
    media = (nota1+nota2) /2
    ficha.append([nome,[nota1,nota2], media])
    r = str(input('Deseja continuar? (S/N)'))
    if r not in 'Ss':
        break

print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-=' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*35)
    opc = int(int(input('Mostrar notas de qual aluno? (999 interrompe)')))
    if opc == 999:
        print('Finalizando...')
        break
    if opc <= len(ficha) -1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')






