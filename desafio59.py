val1 = float(input("Escreva o 1 valor "))
val2 = float(input("Escreva o 2 valor "))
soma = val1 + val2
maior = val1
multiplicacao = val1 * val2
opcao = 1

while opcao != 5:
    opcao = int(input("""Escolha uma das opções abaixo:
[1]Somar
[2]multiplicar
[3]maior
[4]novos números
[5]sair do programa

"""))
    if opcao == 1:
        print(F'A soma dos números é {soma}')
    elif opcao == 2:
        print(F'A multiplicação dos números é {multiplicacao}')
    elif opcao == 3:
        if val2 > val1:
            maior = val2
        print(F'O maior valor é {maior}')
    elif opcao == 4:
        print("Escolha novos valores")
        val1 = input("Escreva o 1 valor ")
        val2 = input("Escreva o 2 valor ")
    elif opcao !=5:
        print('Você digitou um valor invalido')
print("Você saiu do programa")
