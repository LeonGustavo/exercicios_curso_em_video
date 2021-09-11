from operator import itemgetter
from random import randint
from time import sleep

jogo = {
    'Jogador1': randint(1,6),
    'Jogador2': randint(1,6),
    'Jogador3': randint(1,6),
    'Jogador4': randint(1,6)
        }
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado')

ranking = sorted(jogo.items(), key=itemgetter(1),reverse=True)
print('ORDEM DE VENCEDORES')
for i, v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} com {v[1]}')



