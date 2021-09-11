from random import randint

val1= int(input(""" 
Escolha uma opção:
1 - Pedra
2 - Papel
3 - Tesoura

"""))


val2 = randint(1, 3)

if val1 == val2:
    print(F'Empatou!, Você escolheu {val1} e o computador escolheu {val2}')
elif val1 == 1 and val2 == 3:
    print(F'Você ganhou!, Você escolheu {val1} e o computador escolheu {val2}')
elif val1 == 2 and val2 == 1:
    print(F'Você ganhou!, Você escolheu {val1} e o computador escolheu {val2}')
elif val1 == 3 and val2 == 2:
    print(F'Você ganhou!, Você escolheu {val1} e o computador escolheu {val2}')
else:
    print(F'Você perdeu!, Você escolheu {val1} e o computador escolheu {val2}')

