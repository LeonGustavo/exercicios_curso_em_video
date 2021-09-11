valor = 0
pi = 0
pf = 0

valor = str(input('Digite sua expressão '))
pi = valor.count(')')
pf = valor.count('(')

if valor.index(')') > valor.index('('):
    if pi == pf:
        print('Expressão válida')
    else:
        print('Expressão é inválida')
else:
    print('Expressão inválida')



