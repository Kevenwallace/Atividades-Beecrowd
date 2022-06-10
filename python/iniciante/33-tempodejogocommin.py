

con = 0
count = 0

hrs = input()
hrs = hrs.split(None)

start = int(hrs[0])
starmin = int(hrs[1])
end = int(hrs[2])
endmin = int(hrs[3])

count = start

while True:
     count += 1
     con +=1
     if count == 24:
         count = 0
     if count == end:
         break

mino = con * 60

maior = starmin
menor = endmin
if endmin > maior:
    maior = endmin
    menor = starmin

if starmin > endmin:
    minus = mino - (maior - menor)
else:
    minus = mino + (maior - menor)

horas = minus // 60
minutos = minus % 60
lim = horas + (minutos / 60)
if minus > 1440:
    horas = 0


print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")