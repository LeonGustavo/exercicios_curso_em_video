from random import shuffle,choices

a1 = str(input('Diga o nome do primeiro aluno'))
a2 = str(input('Diga o nome do segundo aluno'))
a3 = str(input('Diga o nome do terceiro aluno'))
a4 = str(input('Diga o nome do quarto aluno'))

a5 = [a1, a2, a3, a4]
a6= choices(a5,k=4)

print(F'A ordem de apresentação será: {a6}')

