frase = input('Escreva uma frase')
frase1 = frase.replace(' ','').upper()
frase2 = ''

for c in range(len(frase1) -1, -1, -1):
    frase2 += frase1[c]
print(frase1, frase2)
if frase1 == frase2:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')