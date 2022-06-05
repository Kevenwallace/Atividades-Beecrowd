"""
Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.

Entrada

O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um item conforme tabela acima.
Saída

O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casas após o ponto decimal.


    item 1 = cachorro quente = R$ 4.00
    item 2 = X-salada        = R$ 4.50
    item 3 = X-Bacon         = R$ 5.00
    item 4 = Torrada simples = R$ 2.00
    item 5 = refrigerante    = R$ 1.50"""

valores = {1: 4.00, 2: 4.50, 3: 5.00, 4: 2.00, 5: 1.50}

pedido = input()
pedido = pedido.split(None)
item = int(pedido[0])
quant = int(pedido[1])

preco = valores[item] * quant
print(f"Total: R$ {preco:.2f}")