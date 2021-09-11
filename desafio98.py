def contador(inicio, fim, passo):
    if inicio > fim:
        passo = passo*(-1)
    print(f'Contando {inicio} até {fim} de {passo} em {passo} ')
    for a in range(inicio, fim + 1, passo):
        print(f'{a} ', end='')
    print()


contador(1, 10, 1)
contador(10, 0, 2)
