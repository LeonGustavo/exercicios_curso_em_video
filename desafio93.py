jogador = {}
gols =[]

jogador['nome'] = str(input('Nome do jogador'))
jogador['partidas'] = int(input('Quantas partidas ele jogou?'))

for v in range(0, jogador['partidas']):
    gols.append(int(input(f'Quantos gols o jogador fez na partida {v+1}? ')))
jogador['gols'] = gols.copy()
jogador['total'] = sum(jogador['gols'])
print(jogador)
print('-='*30)
for k,i in jogador.items():
    print(f'O campo {k} tem o valor {i}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas')
for k in range(0, jogador["partidas"]):
    print(f'Na partida {k+1} , fez {jogador["gols"][k]} gols ')
print(f'Foi um total de {jogador["total"]} gols')





