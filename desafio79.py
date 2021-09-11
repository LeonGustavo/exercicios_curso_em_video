lista = []
while True:
    n = int(input('Digite um número para a lista '))
    if n not in lista:
        lista.append(n)
    r= str(input('Quer continuar? [S/N]'))
    if r in 'Nn':
        break
print(F'Os valores digitados são {lista}')
lista.sort()
print(F'E os valores em ordem crescente são {lista}')

