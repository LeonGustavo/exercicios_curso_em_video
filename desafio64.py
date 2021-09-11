soma = -999
total = -1
valor = 0

while valor != 999:
    valor = int(input("Digite um valor para a soma ou 999 para parar "))
    soma += valor
    total +=1
print(F'Você digitou {total} números e a soma é {soma}')