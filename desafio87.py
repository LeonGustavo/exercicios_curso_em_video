matriz = [[0,0,0],[0,0,0],[0,0,0]]
total = tot3 = maior2 = 0

for a in range(0,3): #linha
    for b in range(0,3): #coluna

        matriz[a][b] = int(input(f'Digite um valor para [{a,b}]'))
        if matriz[a][b]%2 == 0:
            total += 1
        if b == 2:
            tot3 += matriz[a][b]
        if a == 1:
            if matriz[a][b] > maior2:
                maior2 = matriz[a][b]


for v in range(0,3):
    print(matriz[v])
print(f'A soma dos valores pares é: {total}')
print(f'A soma dos valores da terceira coluna é: {tot3}')
print(f'O maior valor da segunda linha é: {maior2}')