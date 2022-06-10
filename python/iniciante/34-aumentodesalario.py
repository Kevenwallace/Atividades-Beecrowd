slrio = float(input())

def salario(salario, porcento):
    porct = ((salario*porcento)/100)
    salarioplus = salario + porct
    print(f"Novo salario: {salarioplus:.2f}")
    print(f"Reajuste ganho: {porct:.2f}")
    print(f"Em percentual: {porcento}%")

if slrio >= 0:
    if slrio <= 400.00:
        salario(slrio, 15)
    elif slrio <= 800.00:
        salario(slrio, 12)
    elif slrio <= 1200.00:
        salario(slrio, 10)
    elif slrio <= 2000.00:
        salario(slrio, 7)
    elif slrio > 2000.00:
        salario(slrio, 4)

else:
    exit()    



    