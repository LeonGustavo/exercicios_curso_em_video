valor= float(input("Qual o valor da casa?"))
sal= float(input("Qual o seu salário?"))
anos= int(input("Em quantos anos você irá pagar?"))

vparcela= (valor/(anos*12))


if vparcela < sal*0.30:
    print(F'O empréstimo foi aprovado, {anos * 12} prestações de {vparcela}')


else:
    print("O emprestimo não foi aprovado")