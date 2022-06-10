"""
Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente, de modo que o lado A representa o maior dos 3 lados. A seguir, determine o tipo de triângulo que estes três lados formam, com base nos seguintes casos, sempre escrevendo uma mensagem adequada:

    se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
    se A2 = B2 + C2, apresente a mensagem: TRIANGULO RETANGULO
    se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO
    se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO
    se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
    se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES
"""
i = 0
ordem = list()
num = input()
num = num.split(None)
for i in range(len(num)):
    ordem.append(float(num[i]))

ordem.sort(reverse=True)

A = ordem[0]
B = ordem[1]
C = ordem[2]

if ((B-C)<A<(B+C)) and ((A-C)<B<(A+B)) and ((A-B)<C<(A+B)):
    if A >= B+C:
        print("NAO FORMA TRIANGULO")
        triangulo = False
    else:
        triangulo = True
        if (A**2) == ((B**2)+ (C**2)):
            print("TRIANGULO RETANGULO")    
        elif (A**2) > ((B**2)+ (C**2)):
            print("TRIANGULO OBTUSANGULO")
        elif (A**2) < ((B**2) + (C**2)):
            print("TRIANGULO ACUTANGULO")
        
    if triangulo == True:
        if A == B == C:
            print("TRIANGULO EQUILATERO")
        else:
            if (A == B) or (A == C) or (B == C):
                print("TRIANGULO ISOSCELES")    
else:
    print("Não forma triangulo")