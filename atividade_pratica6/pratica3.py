"""
Desenvolva um programa que consulta dados de endereço a partir de um CEP brasileiro. Siga os passos abaixo:

* Solicite ao usuário que digite um CEP (apenas números, sem traço).  
* Acesse a API pública do ViaCEP: "https://viacep.com.br/ws/{cep}/json/".  
* Exiba as seguintes informações: logradouro, bairro, cidade, estado e o próprio CEP.  
* Caso o CEP não exista ou haja erro, informe isso de forma clara ao usuário.  

Dica: Use o módulo `requests` e trate exceções com `try/except`.
"""

import requests

def consultar_cep():
    
    while True:
        cep = input("Digite o CEP (apenas números, sem traço): ")

        
        if not cep.isdigit() or len(cep) != 8:
            print("CEP inválido. Por favor, digite 8 dígitos numéricos.")
            continue
        break

    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        
        if 'erro' in data and data['erro']:
            print(f"CEP '{cep}' não encontrado ou inválido.")
        else:
            print("Informações do Endereço:")
            print(f"CEP: {data.get('cep', 'N/A')}")
            print(f"Logradouro: {data.get('logradouro', 'N/A')}")
            print(f"Bairro: {data.get('bairro', 'N/A')}")
            print(f"Cidade: {data.get('localidade', 'N/A')}")
            print(f"Estado: {data.get('uf', 'N/A')}")

    except requests.exceptions.RequestException as erro:
        print(f"Erro de conexão com a API ViaCEP: {erro}")
    except ValueError:
        print("Erro ao decodificar a resposta da API (formato JSON inválido).")
    except Exception as erro:
        print(f"Ocorreu um erro inesperado: {erro}")

if __name__ == "__main__":
    consultar_cep()