"""1- Conversor de Moeda
Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

* Valor em reais: R$ 100.00
* Taxa do dólar: R$ 5.20
* Taxa do euro: R$ 6.15
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais."""

valor_real = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

valor_dolar = valor_real / taxa_dolar
valor_euro = valor_real / taxa_euro


print(f"Valor em reais: R$ {valor_real:.2f}")
print(f"Convertido para dólar: US$ {valor_dolar:.2f}")
print(f"Convertido para euro: € {valor_euro:.2f}")