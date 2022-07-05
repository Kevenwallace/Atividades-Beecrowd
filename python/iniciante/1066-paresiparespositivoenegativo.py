num = list()
for c in range(0, 5):
    num.append(int(input()))

contp = 0
countpar = 0
negativo = 0
for n in num:
    if n > 0:
        contp += 1
    if n < 0:
        negativo +=1
    if n % 2 == 0:
        countpar +=1
    


positivo = contp
par = countpar
impar = len(num) - par

print(f"{par} valor(es) par(es)")
print(f"{impar} valor(es) impar(es)")
print(f"{positivo} valor(es) positivo(s)")
print(f"{negativo} valor(es) negativo(s)")