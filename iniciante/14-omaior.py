"""

Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula:

Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo, portanto é necessário para chegar no resultado esperado.
Entrada

O arquivo de entrada contém três valores inteiros.
Saída

Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".
"""

num = input()

nume = num.split(None)

A = int(nume[0])
B = int(nume[1])
C = int(nume[2])

M = (A + B + abs(A - B))/2
maxi = (M + C + abs(M - C))/2

print(f"{maxi:.0f} eh o maior")