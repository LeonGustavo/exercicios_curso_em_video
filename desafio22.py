nome= input("Escreva seu nome").strip()
nomesplit= nome.split()


print(F'{nome.upper()}')
print(F'{nome.lower()}')
print(F'O nome possui {len(nome)- nome.count(" ")} letras')
print(F"O primeiro nome possui {len(nomesplit[0])} letras")

