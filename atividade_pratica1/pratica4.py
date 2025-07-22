"""4- Calculadora de Preço Total
* Desenvolva um programa que calcula o preço total de uma compra. Use as seguintes informações:

* Nome do produto: "Cadeira Infantil"
* Preço unitário: R$ 12.40
* Quantidade: 3
O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final."""

nome_do_produto = "Cadeira Infantil"
preco_unitario = 12.40
quantidade = 3

preco_total = preco_unitario * quantidade

print ("Nome do Produto:", nome_do_produto)
print ("Preço Unitário: R${:.2f}" .format(preco_unitario))
print("Quantidade:", quantidade)

print("Preço Total: R${:.2f}" .format(preco_total))