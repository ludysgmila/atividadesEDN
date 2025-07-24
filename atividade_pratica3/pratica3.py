"""3- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter."""


temperatura = float(input("Digite a temperatura: "))
origem = input("Digite a unidade de origem (C, F ou K): ").upper()
destino = input("Digite a unidade de destino (C, F ou K): ").upper()

if origem == "C":
    if destino == "F":
        resultado_temperatura = (temperatura * 9/5) + 32
    elif destino == "K":
        resultado_temperatura = temperatura + 273.15
    else:
        resultado_temperatura = temperatura

elif origem == "F":
    if destino == "C":
        resultado_temperatura = (temperatura - 32) * 5/9
    elif destino == "K":
        resultado_temperatura = (temperatura - 32) * 5/9 + 273.15
    else:
        resultado_temperatura = temperatura

elif origem == "K":
    if destino == "C":
        resultado_temperatura = temperatura - 273.15
    elif destino == "F":
        resultado_temperatura = (temperatura - 273.15) * 9/5 + 32
    else:
        resultado_temperatura = temperatura

print(f"{temperatura}°{origem} é igual a {resultado_temperatura:.2f}°{destino}")