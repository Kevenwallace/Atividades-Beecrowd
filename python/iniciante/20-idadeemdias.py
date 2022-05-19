"""

Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias

Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias. Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364. Este é apenas um exercício com objetivo de testar raciocínio matemático simples.
Entrada

O arquivo de entrada contém um valor inteiro.
Saída

Imprima a saída conforme exemplo fornecido.
"""

dia = int(input())
mes = 0
anos = 0
while True:
    if dia >= 365:
        anos += 1
        dia -= 365
    elif dia >= 30:
        mes += 1
        dia -= 30
    else:
        break


print(f"""{anos} ano(s)
{mes} mes(es)
{dia} dia(s)""")