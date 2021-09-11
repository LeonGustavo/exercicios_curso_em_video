lista = []
cont = 0
while True:
    n = int(input('Digite um número para incluir na lista '))
    lista.append(n)
    cont += 1
    r = str(input('Quer continuar? [S/N]'))
    if r in 'Nn':
        break

print(f'Foram digitados {cont} números')
lista.sort(reverse=True)
print(f'A lista em forma decrescente é {lista}')
if 5 in lista:
    print('O número 5 está na lista')
else:
    print('O número 5 não está na lista')
