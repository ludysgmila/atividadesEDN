"""4- Calculadora de Idade em Dias
Crie um programa que calcula a idade aproximada de uma pessoa em dias. Para isso:

* Solicite o ano de nascimento da pessoa.  
* Considere o ano atual automaticamente.  
* Calcule a idade em anos e transforme em dias (desconsidere anos bissextos).  
* Exiba o resultado final."""

import datetime

def calcular_idade (ano_nascimento):
    hoje = datetime.datetime.today().date()
    data_nascimento = datetime.date(ano_nascimento, 1, 1)
    diferenca = hoje - data_nascimento
    return diferenca.days

try:
    ano_nascimento = int(input("Digite o ano do seu nascimento: "))
    ano_atual = datetime.datetime.today().year

    if ano_nascimento > ano_atual or ano_nascimento < 1900:
        print("Ano de nascimento inválido.")
    else:
        idade_dias = calcular_idade (ano_nascimento)
        print(f"Sua idade aproximada em dias, considerando anos bissextos): {idade_dias} dias.")

except ValueError:
    print("Erro: você deve digitar um número válido para o ano.")


