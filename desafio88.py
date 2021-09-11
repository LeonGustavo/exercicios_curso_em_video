from random import randint
from time import sleep
mega = []
jogos = []
print('-'*30)
print('   MEGA    ')
print('-'*30)
quant = int(input('Quantos jogos voce quer sortear?'))
tot = 1
while tot <= quant:
    cont= 0
    while True:
        n = randint(1,60)
        if n not in mega:
            mega.append(n)
            cont+= 1
        if cont>=6:
            break
    mega.sort()
    jogos.append(mega[:])
    mega.clear()
    tot += 1
print('-='*3, f'Sorteando {quant} jogos', '-='*3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)


