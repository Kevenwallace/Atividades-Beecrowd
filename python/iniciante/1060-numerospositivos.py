"""
Faça um programa que leia 6 valores. Estes valores serão somente negativos ou positivos (desconsidere os valores nulos). A seguir, mostre a quantidade de valores positivos digitados."""

count = 0
positivo = 0
while count < 6:
    n = float(input())
    if n > 0:
        positivo += 1
    count += 1

print(f"{positivo} valores positivos")  