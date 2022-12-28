"""Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos números impares entre eles.

Entrada
O arquivo de entrada contém dois valores inteiros.

Saída
O programa deve imprimir um valor inteiro. Este valor é a soma dos valores ímpares que estão entre os valores fornecidos na entrada que deverá caber em um inteiro."""



#value = input()
#value = value.split()
#num1, num2 = value

num1 = int(input())
num2 = int(input())

if num1 == num2:
    print('0')
else:
    if num1 < num2:
        menor = num1
        maior = num2
    else:
        menor = num2
        maior = num1

    soma = 0
    for x in range(menor+1, maior):
        if (x%2) != 0:
            soma = soma + x
    print(soma)