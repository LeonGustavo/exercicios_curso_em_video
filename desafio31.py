dist = int(input("Qual a distancia da viagem "))

if dist <= 200:
    print(F'A viagem ficou R${dist*0.50}')
else: print(F'A viagem ficou mais barata R${dist*0.45}')