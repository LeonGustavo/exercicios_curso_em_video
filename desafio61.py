primeiroT = int(input("Qual é o primeiro termo da PA "))
razao = int(input("Qual é a razao da PA "))
decimo = primeiroT + (10-1) *razao
cont = primeiroT

while cont < decimo:

    cont += razao
    print(F'{cont-razao},')



