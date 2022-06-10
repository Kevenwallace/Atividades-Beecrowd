"""
Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas.
Entrada

A entrada contém dois valores inteiros representando a hora de início e a hora de fim do jogo.
Saída

Apresente a duração do jogo conforme exemplo abaixo.
"""
con = 0
count = 0

hrs = input()
hrs = hrs.split(None)

start = int(hrs[0])
end = int(hrs[1])
count = start

while True:
     count += 1
     con +=1
     if count == 24:
         count = 0
     if count == end:
         break


print(f"O JOGO DUROU {con} HORA(S)")
