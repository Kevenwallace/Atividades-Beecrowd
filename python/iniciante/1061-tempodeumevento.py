diasart = input()
diasart = diasart.split(None)
dia1 = int(diasart[1])

hrsstart = input()
hrsstart = hrsstart.split(":")

hrs1 = int(hrsstart[0])
min1 = int(hrsstart[1])
seg1 = int(hrsstart[2])

#"-----------------------------------------------"
diaend = input()
diaend = diaend.split(None)
dia2 = int(diaend[1])

hrsend = input()
hrsend = hrsend.split(":")

hrs2 = int(hrsend[0])
min2 = int(hrsend[1])
seg2 = int(hrsend[2])
#"-----------------------------------------------"
segundos = 0
minutos = 0
horas = 0


segundos = seg2 - seg1

if segundos < 0:
    segundos += 60
    minutos -= 1

minutos = minutos + (min2 - min1)

if minutos < 0:
    minutos += 60
    horas -= 1

dias =  dia2 - dia1

horas = horas + (hrs2 - hrs1)

if horas < 0:
    horas += 24
    dias -= 1





print(f"{dias} dia(s)")
print(f"{horas} hora(s)")
print(f"{minutos} minuto(s)")
print(f"{segundos} segundo(s)")


    