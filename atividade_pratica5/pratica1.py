"""1- Calculadora de Gorjeta
Crie um programa que calcula o valor da gorjeta a partir do total da conta e da porcentagem escolhida. Use as instruções abaixo:

* Defina o valor da conta (ex: R$ 100,00).  
* Informe a porcentagem da gorjeta (ex: 10%, 15%, 20%).  
* O programa deve calcular o valor correspondente e exibir o resultado com duas casas decimais."""

def calcular_gorjeta(valor_conta, opcao):
    if opcao == "1":
        porcentagem = 10
    elif opcao == "2":
        porcentagem = 15
    elif opcao == "3":
        porcentagem = 20
    else:
        print("Opção inválida. Usando porcentagem padrão de 10%.")
        porcentagem = 10

    gorjeta = valor_conta * (porcentagem / 100)
    total = valor_conta + gorjeta
    print(f"Valor total a pagar com a gorjeta: R$ {total:.2f}")


valor_conta = float(input("Digite o valor da conta: R$ "))
opcao = input("Escolha a porcentagem da gorjeta (1- 10%, 2- 15% ou 3- 20%): ")

calcular_gorjeta(valor_conta, opcao)