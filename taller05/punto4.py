print("==========================================")
print("==========================================")
print("Calculador salarial en la semana laburada")
print("=========================================")

salario = float(input("Ingrese la tarifa por hora: "))
horas = float(input("Ingrese el numero de horas que trabajo en la semana: "))
horasExtra = 0
salarioExtra = 0
salarioNormal = horas*salario

if horas>=41:
    horasExtra = horas-40
    salario = salario*50/100
    salarioExtra = horasExtra*salario
    totalSalario = salarioNormal+salarioExtra
    print("El total del salario a la semana mas las horas extra es: ",round(totalSalario))
    
else:
    print("El total del salario a la semana es: ",round(salarioNormal))