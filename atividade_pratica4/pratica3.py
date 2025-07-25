"""3- Verificador de Senhas Fortes
Crie um programa que avalia a força de uma senha informada pelo usuário. O programa deve:

* Solicitar a senha até que o usuário digite "sair".  
* Verificar se a senha possui pelo menos 8 caracteres.  
* Verificar se contém pelo menos um número.  
* Informar se a senha é fraca ou forte.  
* Encerrar o programa apenas quando a senha for forte ou se o usuário digitar "sair". """

while True:
    senha = input("Digite uma senha ou se desejar, 'sair' para encerrar): ")

    if senha == "sair":
        print("Programa encerrado.")
        break

    contador_caracteres = 0
    for _ in senha:
        contador_caracteres += 1

    tem_tamanho = False
    if contador_caracteres >= 8:
        tem_tamanho = True

    tem_numero = False
    for caractere in senha:
        if caractere in "0123456789":
            tem_numero = True
            break

    
    if tem_tamanho and tem_numero:
        print("Senha forte!")
        break
    else:
        print("Senha fraca. A senha precisa ter pelo menos 8 caracteres e conter pelo menos um número.")