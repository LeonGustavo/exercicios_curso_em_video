soma = 0
cont = 0
for c in range(1,7):
    val = int(input(F'Digite o {c}* valor '))
    if val % 2 == 0:
        soma += val
        cont += 1
print(F'Você informou {cont} números PARES e a soma foi {soma}')