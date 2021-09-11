from datetime import date

anoNasc= int(input("Qual o seu ano de nascimento"))
idade = (date.today().year)-anoNasc

if idade < 9:
    print("MIRIM")
elif idade < 14:
    print("INFANTIL")
elif idade < 19:
    print("SÊNIOR")
else:
    print("MASTER")


