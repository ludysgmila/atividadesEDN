'''
Crie um programa que escreve dados de pessoas (nome, idade e cidade) em um arquivo CSV. Para isso:

* Crie uma lista de listas com dados fictícios de pelo menos três pessoas.  
* Solicite ao usuário o nome do arquivo CSV onde os dados serão salvos.  
* Escreva os dados usando o módulo `csv`, com cabeçalhos apropriados.  
* Confirme a gravação exibindo uma mensagem com o nome do arquivo.  
* Trate possíveis erros de escrita de arquivo.

Dica: Use `csv.writer()` para escrever os dados linha por linha.
'''

import csv

def criar_e_salvar_csv():

    dados_pessoas = [
        ["Nome", "Idade", "Cidade"],
        ["Lalisa Manoban", 28, "Bangok"],
        ["Camila Cabello", 30, "Havana"],
        ["Jennie Ruby Jane", 29, "Seul"]
    ]

    nome_arquivo = input("Por favor, digite o nome do arquivo CSV para salvar (ex: pessoas.csv): ")

    try:
        with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
            escritor = csv.writer(arquivo_csv)
            for linha in dados_pessoas:
                escritor.writerow(linha)
        print(f"Dados salvos com sucesso no arquivo '{nome_arquivo}'!")

    except IOError as e:
        print(f"Erro de E/S ao tentar escrever no arquivo '{nome_arquivo}': {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

criar_e_salvar_csv()