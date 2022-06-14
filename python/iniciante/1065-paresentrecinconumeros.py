num = list()
count = 0

for c in range(0, 5):
    num.append(float(input()))

for n in num:
    if n % 2 == 0:
        count +=1
    
print(f"{count} valores pares")

