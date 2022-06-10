"""


Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.
Entrada

O arquivo de entrada contém um valor inteiro N.
Saída

Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo fornecido.
"""

seg = int(input())
minu = 0
hora = 0
while True:
    if seg >= 60:
        minu = minu + 1
        seg -= 60
    elif minu >= 60:
        hora += 1
        minu -= 60
    else:
        break



print(f"{hora}:{minu}:{seg}")