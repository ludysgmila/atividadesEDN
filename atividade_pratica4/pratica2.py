"""2- Registro de Notas e Cálculo da Média
Desenvolva um programa para registrar notas de uma turma e calcular a média final. Siga as instruções abaixo:

* O programa deve solicitar notas continuamente até o usuário digitar "fim".  
* Somente notas entre 0 e 10 devem ser aceitas.  
* Ao final, exiba a média da turma com duas casas decimais e o total de notas válidas registradas.  
* Trate entradas inválidas com mensagens de erro.""" 



total_notas = 0 
quantidade_notas = 0  

while True:
    entrada = input("Digite uma nota e 'fim' para encerrar): ")

    if entrada == "fim":
        break

    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            total_notas += nota       
            quantidade_notas += 1      
        else:
            print("Erro: A nota deve estar entre 0 e 10.")
    except ValueError:
        print("Erro: Entrada inválida. Digite um número ou 'fim'.")

if quantidade_notas > 0:
    media = total_notas / quantidade_notas
    print(f"Média da turma: {media:.2f}")
    print(f"Total de notas válidas registradas: {quantidade_notas}")
else:
    print("Nenhuma nota válida foi registrada.")