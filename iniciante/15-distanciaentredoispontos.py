"""

Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais após a vírgula, segundo a fórmula:

Distancia =
Entrada

O arquivo de entrada contém duas linhas de dados. A primeira linha contém dois valores de ponto flutuante: x1 y1 e a segunda linha contém dois valores de ponto flutuante x2 y2.
Saída

Calcule e imprima o valor da distância segundo a fórmula fornecida, com 4 casas após o ponto decimal.
"""


num1 = input()
num2 = input()

number1 = num1.split(None)
number2 = num2.split(None)

x1 = float(number1[0])
y1 = float(number1[1])

x2 = float(number2[0])
y2 = float(number2[1])

raizquadrada = 1/2
distancia = ((x2 - x1)**2 + (y2 - y1)**2)**raizquadrada
 

print(f"{distancia:.4f}")