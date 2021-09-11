sexo = str(input("Informe o sexo (M ou F) ")).upper().strip()
while sexo not in 'MmFf':
    sexo = str(input('Digite o sexo corretamente ')).upper()
    print(F'{sexo}')
print(F'O sexo escolhido é  {sexo}')
