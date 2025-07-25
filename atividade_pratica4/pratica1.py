"""1- Calculadora Simples
Crie um programa que simule uma calculadora básica com as seguintes funcionalidades:

* Solicite ao usuário dois números reais.  
* Peça a operação desejada (+, -, *, /).  
* Realize a operação escolhida e exiba o resultado.  
* Trate divisões por zero e operações inválidas com mensagens apropriadas.  

O programa deve continuar solicitando entradas até que uma operação válida seja realizada com sucesso."""

questao = int(input("Desejar começar? se sim digite (1), se não digite (0)?"))
while questao == 1:

    numero1 = int(input("Digite o primeiro número:"))
    numero2 = int(input("Digite o segundo número:"))

    operacao = input ("Escolha a operação (+, -, *, /): ")

    if numero1 == 0 and numero2== 0:
        print("Valor inválido. Por favor, insira um valor valido.")

    else:

        if operacao == "+":
            soma = numero1 + numero2
            print("Resultado: ", soma)

        elif operacao == "-":
            subtracao = numero1 - numero2
            print("Resultado:", subtracao)
                
        elif operacao == "*":
            multiplicacao = numero1 * numero2
            print("Resultado:", multiplicacao)
                    
        elif operacao == "/":
            if numero2 == 0:
                print("divisão por zero não é permitida, tente outro número")

        else:
                    divisao = numero1 / numero2 
                    print("Resultado:", divisao)

    questao = int(input("Desejar começar novamente? se sim digite (1), se não digite (0)?"))
    print("Obrigada por utilizar nossa calculadora!")

        
                
    
    






