primeiro = int(input("Qual é o primeiro termo da PA "))
razao = int(input("Qual é a razao da PA "))
termo = primeiro
cont = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print(F'{termo},')
        termo += razao
        cont += 1
    mais = int(input("Você deseja mostrar mais quantos termos?"))




