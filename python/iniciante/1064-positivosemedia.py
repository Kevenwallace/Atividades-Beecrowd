num = list()
count = 0
soma = 0

for c in range(0, 6):
    num.append(float(input()))

for n in num:
    if n > 0:
        count +=1
        soma += n

media  = soma/count
print(f"{count} valores positivos")
print(media)