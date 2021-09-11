from random import choice

a1 = input('Diga o nome do primeiro aluno')
a2 = input('Diga o nome do segundo aluno')
a3 = input('Diga o nome do terceiro aluno')
a4 = input('Diga o nome do quarto aluno')

a5 = [a1, a2, a3, a4]

print(F'O aluno sorteado foi {choice(a5)}')
