numero= int(input("Digite o numero de elementos "))
a = [1,1]
cont = 2
cont2 = 0

while cont < (numero):
    a.append((a[cont-1]) + (a[cont-2]))
    print(F'{a[cont2]}')
    cont += 1
    cont2 += 1







