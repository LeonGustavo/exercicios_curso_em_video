from datetime import date
pessoa = {}
a = date.today()


pessoa['nome'] = str(input('Qual o nome seu nome?'))
b = int(input('Qual o seu ano de nascimento?'))
pessoa['idade'] = (a.year-b)
pessoa['ctps'] = int(input('Numero da CTPS / 0 se não possuir'))

if pessoa['ctps'] != 0:
    pessoa['anocontratacao'] = int(input('Qual o ano de contratação?'))
    pessoa['salario'] = float(input('Qual o salário?'))
    pessoa['aposentadoria'] = pessoa['idade'] + ((pessoa['anocontratacao'] +35) -a.year)

for k,i in pessoa.items():
    print(f'{k} tem o valor {i}')

