"""4- Analisador de Números Pares e Ímpares
Desenvolva um programa que classifica números inteiros como pares ou ímpares. O programa deve:

* Solicitar números inteiros até que o usuário digite "fim".  
* Informar se o número digitado é par ou ímpar.  
* Ao final, exibir a quantidade total de números pares e ímpares informados.  
* Tratar entradas inválidas com mensagens de erro apropriadas.  """

quantidade_pares = 0
quantidade_impares = 0

while True:
    entrada = input("Digite um número inteiro ou se desejar, 'fim' para encerrar): ")

    if entrada == "fim":
        break

    try:
        numero = int(entrada)

        if numero % 2 == 0:
            print("O número é par.")
            quantidade_pares += 1
        else:
            print("O número é ímpar.")
            quantidade_impares += 1

    except ValueError:
        print("Erro: Entrada inválida. Digite apenas números inteiros ou 'fim'.")

print("Análise concluída:")
print("Quantidade de números pares:", quantidade_pares)
print("Quantidade de números ímpares:", quantidade_impares)