var= input("Escreva uma frase")
letra = var.find("a")

print(F'A letra "a" aparece {var.count("a")} vezes')

print(F'A letra apareceu a primeira vez na posição {letra+1}')

print(F'A letra apareceu a ultima vez na posição {var.rfind("a")+1}')