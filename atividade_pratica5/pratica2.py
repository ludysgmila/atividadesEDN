"""2- Verificador de Palíndromos
Crie um programa que verifica se uma palavra ou frase é um palíndromo, ou seja, se pode ser lida da mesma forma de trás para frente, desconsiderando espaços, acentos e pontuação. Para isso:

*Solicite ao usuário uma palavra ou frase.
*Desconsidere letras maiúsculas, espaços e sinais de pontuação.
*Verifique se a frase é um palíndromo.
*Exiba "Sim" se for palíndromo ou "Não" se não for."""

import unicodedata

def limpar(frase):
    frase = frase.lower()  
    nova_frase = ""
    for letra in frase:
        if letra.isalnum(): 
            nova_frase += letra
    return nova_frase


def verificar_palindromo(frase):
    frase_limpa = limpar(frase)
    if frase_limpa == frase_limpa[::-1]:
        return True
    else:
        return False

texto = input("Digite uma palavra ou frase: ")

if verificar_palindromo(texto):
    print("Sim, é um palindromo")
else:
    print("Não é palindromo")