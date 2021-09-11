num = int(input("Escreva um número inteiro qualquer "))
val = 0
fat = num

while num != 1:
    fat += fat*(num-2)
    num = num-1
print(F'{fat}')
