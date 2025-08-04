'''
Desenvolva um programa que lê os dados de um arquivo CSV e imprime cada linha na tela. Para isso:

* Solicite ao usuário o nome do arquivo CSV a ser lido.  
* Utilize o módulo `csv` para abrir o arquivo e ler os dados.  
* Exiba cada linha completa como uma lista.  
* Trate erros como arquivo inexistente ou problemas na leitura.

Dica: Use `csv.reader()` para ler e percorrer as linhas do arquivo.
'''
import csv
import os

def ler_imprimir_csv():

    nome_arquivo = input("Por favor, digite o nome do arquivo CSV para ler (ex: dados.csv): ")

    if not os.path.exists(nome_arquivo):
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado. Verifique o nome e o caminho.")
        return

    try:
        with open(nome_arquivo, mode='r', newline='', encoding='utf-8') as arquivo_csv:
            leitor = csv.reader(arquivo_csv)
            print(f"Conteúdo do arquivo '{nome_arquivo}':")
            for linha in leitor:
                print(linha)

    except IOError as erro:
        print(f"Erro ao tentar ler o arquivo '{nome_arquivo}': {erro}")
    except Exception as erro:
        print(f"Ocorreu um erro inesperado ao ler o arquivo: {erro}")

ler_imprimir_csv()
