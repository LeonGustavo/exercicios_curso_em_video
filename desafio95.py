time = []
jogador = {}
gols =[]

while True:
    jogador.clear()
    gols.clear()
    jogador['nome'] = str(input('Nome do jogador'))
    partidas = int(input('Quantas partidas ele jogou?'))
    for v in range(0, partidas):
        gols.append(int(input(f'Quantos gols o jogador fez na partida {v+1}? ')))
    jogador['gols'] = gols.copy()
    jogador['total'] = sum(jogador['gols'])
    time.append(jogador.copy())
    op = str(input('Deseja continuar [S/N]? ')).strip().upper()
    while op not in 'SsNn':
        op = str(input('Deseja continuar [S/N]? ')).strip().upper()
    if op in 'Nn':
        break
print('-='*30)
print('cod  ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:<5}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca=int(input('Mostrar dados de qual jogador? (999 para sair)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com o código {busca}')
    else:
        print(f'LEVANTAMENTO DO JOGADOR {time[busca]["nome"]} ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    Na partida {i+1} fez {g} gols.')
print('-'*30)







