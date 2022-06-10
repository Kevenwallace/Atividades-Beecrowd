"""
Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram lidos."""


i = 0
num = input()
num = num.split(None)
num[0] = int(num[0])
num[1] = int(num[1])
num[2] = int(num[2])
ordem = num[:]
ordem.sort()

for i in range(len(ordem)):
    print(ordem[i])
print()
i = 0
for i in range(len(num)):
    print(num[i])

