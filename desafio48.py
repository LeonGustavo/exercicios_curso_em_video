cont = 0
for c in range(1, 501, 2):
    if(c % 3 == 0):
        print(F'O valor {c} é multiplo de 3 e irá entrar na soma')
        cont += c
        print(F'{cont}')