ddds = { 61: "Brasilia",
         71: "Salvador",
         11: "Sao Paulo", 
         21: "Rio de Janeiro",
         32: "Juiz de Fora",
         19: "Campinas",
         27: "Vitoria",
         31: "Belo Horizonte"}

num = int(input())

if num in ddds.keys():
    city = ddds[num]
    print(city)
else:
    print("DDD nao cadastrado")