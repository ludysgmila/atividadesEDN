"""
Crie um programa que mostra a cotação atual de moedas estrangeiras em relação ao Real. O programa deve:

* Solicitar ao usuário o código da moeda estrangeira (ex: USD, EUR, GBP).  
* Acessar a API: "https://economia.awesomeapi.com.br/last/{moeda}-BRL".  
* Exibir a cotação atual, o valor máximo, o valor mínimo e a data/hora da última atualização.  
* Informar ao usuário se o código da moeda for inválido ou houver falha na conexão.  

Dica: A conversão da data/hora pode ser feita com o módulo `datetime`.
"""

import requests
from datetime import datetime

def consultar_cotacao():
    moeda = input("Digite o código da moeda estrangeira (ex: USD, EUR, GBP): ").upper()

    url = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"

    try:
        resposta = requests.get(url)
        resposta.raise_for_status()

        dados = resposta.json()

        chave = f"{moeda}BRL"
        if chave not in dados:
            print("Código de moeda inválido ou não suportado.")
            return

        cotacao = dados[chave]
        preco_atual = float(cotacao["bid"])
        preco_max = float(cotacao["high"])
        preco_min = float(cotacao["low"])
        data_hora = datetime.fromtimestamp(int(cotacao["timestamp"])).strftime("%d/%m/%Y %H:%M:%S")

        print(f"Cotação de {moeda} em relação ao Real (BRL):")
        print(f"Preço atual: R$ {preco_atual:.2f}")
        print(f"Valor máximo do dia: R$ {preco_max:.2f}")
        print(f"Valor mínimo do dia: R$ {preco_min:.2f}")
        print(f"Última atualização: {data_hora}")

    except requests.exceptions.RequestException as erro:
        print(f"Erro ao conectar com a API: {erro}")
    except Exception as erro:
        print(f"Ocorreu um erro inesperado: {erro}")
    except ValueError:
        print("Erro ao decodificar a resposta da API. O formato JSON pode estar inválido.")

if __name__ == "__main__":
    consultar_cotacao()