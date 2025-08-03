"""
Crie um programa que acessa uma API pública e exibe informações de um usuário fictício. Para isso:

* Use a API pública "https://randomuser.me/api/" para obter dados aleatórios.  
* Mostre na tela: nome completo, e-mail e país do usuário.  
* O programa deve tratar possíveis erros de conexão ou falha na API.  

Dica: Utilize o módulo `requests` para fazer a requisição e o método `.json()` para acessar os dados.
"""

import requests 

def informacoes_usuario():

    url = "https://randomuser.me/api/"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        usuario = data['results'][0]

        nome_completo = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']

        print(f"Nome Completo: {nome_completo}")
        print(f"E-mail: {email}")
        print(f"País: {pais}")

    except requests.exceptions.ConnectionError:
        print("Erro de conexão: Verifique sua conexão com a internet.")
    except requests.exceptions.Timeout:
        print("Erro de tempo limite: A requisição demorou muito para responder.")
    except requests.exceptions.RequestException as erro:
        print(f"Erro na requisição da API: {erro}")
    except KeyError as erro:
        print(f"Erro ao processar os dados: Chave '{erro}' não encontrada. A estrutura pode ter mudado.")
    except Exception as erro:
        print(f"Ocorreu um erro inesperado: {erro}")

if __name__ == "__main__":
    informacoes_usuario()