slrio = float(input())

def salario(salario, porcento):
    porct = ((salario*porcento)/100)
    return porct

resp = True

if slrio > 4500:
    peso = slrio - 4500
    res = salario(1000, 8)
    res = res + salario(1500, 18)
    res = res + salario(peso, 28)
    

elif 3000 < slrio <= 4500:
    peso = slrio - 3000
    res = salario(1000, 8)
    res = res + salario(peso, 18)
    

elif 2000 < slrio <= 3000:
    peso = slrio - 2000
    res = salario(peso, 8)

else:
    resp = False
    print("Isento")

if resp:
    print(f"R$ {res:.2f}")

