"""
Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.
Entrada

O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).
Saída

Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.

Obs: Utilize ponto (.) para separar a parte decimal.
"""


count = 0
 
valor = str(input())
sub = valor.replace(".", "")
sub = int(sub)
valor = float(sub/100)




cedula = [ 100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print("NOTAS:")
for notas in cedula:
    while True:
        if valor >= notas:
            valor -= notas
            count += 1
        else:
            break            
    print(f"{count} nota(s) de R$ {notas:.2f}")
    count = 0


valor = int(valor * 100)

#a multiplicação por 100 é para não ter erros de arredondamento por conta do float

print("MOEDAS:")
for moeda in moedas:
    while True:
        if valor >= (moeda * 100):
            valor -= (moeda * 100)
            count += 1
        else:
            break
    print(f"{count} moeda(s) de R$ {moeda:.2f}")
    count = 0



