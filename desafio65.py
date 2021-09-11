soma =  0
total = 0
valor = 0
maior = valor
menor = valor
opc= 'SIM'


while opc in 'sSSIMsim':
    valor = int(input("Digite um valor inteiro "))
    soma += valor
    total +=1
    if total == 1:
        maior = menor = valor
    else:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor
    opc = input('Voce deseja continuar? Sim ou Não?').upper()

print(F'Você digitou {total} números e a soma é {soma} e sua média é {soma/total}')
print(F'O maior é {maior} e o menor é {menor}')