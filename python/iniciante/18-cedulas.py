"""


Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.
Entrada

O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).
Saída

Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo fornecido. Não esqueça de imprimir o fim de linha após cada linha, caso contrário seu programa apresentará a mensagem: “Presentation Error”.
"""



valor = -1
count = 0
while valor < 0:    
    valor = int(input())
cedula = {"100": 100, "50": 50, "20": 20, "10": 10, "5": 5, "2": 2, "1": 1}

troco = valor

print(troco)
while True:
    if troco >= cedula["100"]:
        troco -= cedula["100"]
        count += 1
    else: 
        break
print(f"{count} nota(s) de R$ 100,00")
count = 0

while True:
    if 50 <= troco < 100:
        troco -= cedula["50"]
        count += 1
    else:
        break
print(f"{count} nota(s) de R$ 50,00")
count = 0

while True:
    if 20 <= troco < 50:
        troco -= cedula["20"]
        count += 1
    else:
        break
print(f"{count} nota(s) de R$ 20,00")
count = 0

while True:
    if 10 <= troco < 20:
        troco -= cedula["10"]
        count += 1
    else:
        break
print(f"{count} nota(s) de R$ 10,00")
count = 0

while True:
    if 5 <= troco < 10:
        troco -= cedula["5"]
        count += 1
    else:
        break
print(f"{count} nota(s) de R$ 5,00")
count = 0

while True:
    if 2 <= troco < 5:
        troco -= cedula["2"]
        count += 1
    else:
        break
print(f"{count} nota(s) de R$ 2,00")
count = 0

while True:
    if 1 <= troco < 2:
        troco -= cedula["1"]
        count += 1
    else:
        break
print(f"{count} nota(s) de R$ 1,00")
count = 0