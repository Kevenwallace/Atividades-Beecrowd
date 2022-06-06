"""
Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem "Sao Multiplos" ou "Nao sao Multiplos", indicando se os valores lidos são múltiplos entre si.
"""

num = input()
num = num.split(None)
A = int(num[0])
B = int(num[1])

if A > B:
    if A % B == 0:
        print("Sao multiplos")
    else:
        print("Nao sao multiplos")
else:
    if B % A == 0:
        print("Sao multiplos")
    else:
        print("Nao sao multiplos")

