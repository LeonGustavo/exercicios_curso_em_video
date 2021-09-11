# O requests foi instalado a través do pip
# https://docs.python-requests.org/en/master/

import requests


def retorna_dados_cep(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(
        cep))  # com o requests.get foi possível buscar a api do viacep que traz um json com as informaçoes do cep
    print(response.status_code)  # assim é possivel verificar o código de retorno 200 deu certo 400 deu ruim
    print(response.json())  # assim é printado todos os atributos do json
    dados_cep = response.json()
    print(dados_cep['logradouro'])  # o dados_cep recebeu um dicionado do json que pode ser referenciado pelo indice
    print(dados_cep['complemento'])
    return dados_cep


# exemplo de uso de api agora para buscar os dados do pokemon
def retorna_dados_pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    dados_pokemon = response.json()
    return dados_pokemon


def retorna_response(url):
    response = requests.get(url)
    return response.text


if __name__ == '__main__':
    retorna_dados_cep('08275410')

    dados_pokemon = retorna_dados_pokemon('charmander')
    print(dados_pokemon['sprites']['front_shiny'])

    # retorna todo o html da pagina
    response = retorna_response('https://digitalinnovation.one//')
    print(response)
