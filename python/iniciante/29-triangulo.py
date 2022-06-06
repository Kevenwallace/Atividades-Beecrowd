"""
Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:


Perimetro = XX.X


Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem


Area = XX.X

condição de existencia do triangulo{
| b - c | < a < b + c
| a - c | < b < a + c
| a - b | < c < a + b
}
"""

num = input()
num = num.split(None)
A = float(num[0])
B = float(num[1])
C = float(num[2])

if ((B-C)<A<(B+C)) and ((A-C)<B<(A+B)) and ((A-B)<C<(A+B)):
    P = A+B+C
    print(f"Perimetro = {P:.1f}")
else:
    A = ((A+B)*C)/2
    print(f"Area = {A:.1f}")