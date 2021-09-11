km = int(input("Escreva a velocidade do carro"))

if km <= 80:
    print("Você está dentro da velocidade")
else:
    multa= (km-80)*7

    print(F'Você passou do limite de velocidade e irá pagar R$ {multa} de multa')