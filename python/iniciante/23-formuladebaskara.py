"""
Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”, caso haja uma divisão por 0 ou raiz de numero negativo.
Entrada

Leia três valores de ponto flutuante (double) A, B e C.
Saída

Se não houver possibilidade de calcular as raízes, apresente a mensagem "Impossivel calcular". Caso contrário, imprima o resultado das raízes com 5 dígitos após o ponto, com uma mensagem correspondente conforme exemplo abaixo. Imprima sempre o final de linha após cada mensagem.
"""

num= input()
num = num.split(None)
A = float(num[0])
B = float(num[1])
C = float(num[2])

delta = (B ** 2) - (4 * A * C)
if A and B and C != 0:    
    if delta <= 0:
        print("Impossivel calcular")
    else:
        rdelta = (delta ** 0.5)
        r1 = (-B + rdelta) / (2 * A)
        r2 = (-B - rdelta) / (2 * A)
        print(f"R1 = {r1:.5f}")
        print(f"R2 = {r2:.5f}")
else:
    print("Impossivel calcular")