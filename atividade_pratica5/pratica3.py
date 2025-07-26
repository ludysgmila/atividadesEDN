"""3- Calculadora de Desconto em Produto
Desenvolva um programa que aplica um desconto sobre o preço de um produto. O programa deve:

* Solicitar o preço original do produto.  
* Solicitar o percentual de desconto desejado.  
* Calcular e exibir o preço final com desconto, arredondado para duas casas decimais."""

def calcular_desconto(preco, porcentagem):
    if porcentagem < 0 or porcentagem > 100:
        print("Percentual inválido! Deve estar entre 0 e 100.")
        return 0  
    desconto = preco * (porcentagem / 100)
    preco_final = preco - desconto
    return preco_final

try:
    preco_original = float(input("Digite o preço original do produto: R$ "))
    porcentagem_desconto = float(input("Digite o percentual de desconto (%): "))

    if preco_original < 0:
        print("O preço deve ser um número positivo.")
    elif porcentagem_desconto < 0 or porcentagem_desconto > 100:
        print("O percentual de desconto deve estar entre 0 e 100.")
    else:
        preco_com_desconto = calcular_desconto(preco_original, porcentagem_desconto)
        print(f"Preço final com desconto: R$ {preco_com_desconto:.2f}")

except ValueError:
    print("Por favor, digite um número válido.")