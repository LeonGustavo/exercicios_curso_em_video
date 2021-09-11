lista = []
lpar= []
limpar= []

while True:
    n = int(input('Digite um número '))
    lista.append(n)
    r = str(input('Quer continuar? (S/N)'))
    if r not in 'Ss':
        break

for c, v in enumerate(lista):
    if v%2 == 0 :
        lpar.append(v)
    else:
        limpar.append(v)

print(f'Você digitou os números {lista}')
print(f'Dos números digitados os seguintes são pares{lpar}')
print(f'E os seguintes são ímpar{limpar}')