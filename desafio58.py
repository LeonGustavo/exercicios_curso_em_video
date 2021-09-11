from random import randint

palp = int(input('Escolha um número de 1 a 10 '))
pc = randint(1,10)
choice = 0

print(F'O numero do pc é {pc}')
while palp != pc:
        if palp >10:
            print('Você digitou um número invalido')
            palp = int(input('Digite um palpite entre 1 e 10 '))
            choice += 1
        else:
            print('Você errou o palpite')
            choice += 1
            palp = int(input('De um novo palpite entre 1 e 10 '))
print(F'Você acertou o número do pc {pc} com {choice} tentativas')