pessoas = int(input('Quantas pessoas serão pesquisadas '))
ano = ''
menor = 0
maior = 0

for c in range(0, pessoas, 1):
    ano += input(F'Digite a data de nascimento da {c+1}* Pessoa ')

for c in range(0, pessoas,1):
    if ano[c] > 1998:
        maior += 1
    else:
        menor += 1
print(F'Há {maior} pessoas maiores de idade e {menor} menor de idade')

