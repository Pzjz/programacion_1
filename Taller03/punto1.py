print("Calificador del taller")

print("Califica los ejercicios: ")
print("1: Hola mundo")
print("2: Suma de numeros")
print("3.Calcular la edad")
print("4.IMC")
print("5.Hallar numero par e impar")
print("6. hallar el area de un cuadrado")
print("7. hallar el area de un traingulo")
print("8. validar si es mayor o menor de edad:")
print("9. validar aumento de salario: ")
print("10. pago de horas extras:")

n=0
a=int(input("Elige una opcion: "))
if a == 1:
    n=float(input("1: Hola mundo: "))
elif a==2:
    n=float(input("2: Suma de numeros:"))
elif a==3:
    n=float(input("3.Calcular la edad: "))
elif a==4:
    n=float(input("4.IMC: "))
elif a==5:
    n=float(input("5.Hallar numero par e impar: "))
elif a==6:
    n=float(input("6. hallar el area de un cuadrado: "))
elif a==7:
    n=float(input("7. hallar el area de un traingulo: "))
elif a==8:
    n=float(input("8. validar si es mayor o menor de edad: "))
elif a==9:
    n=float(input("9. validar aumento de salario: "))
elif a==10:
    n=float(input("10. pago de horas extras: "))
else: 
    print("Error")

print("Calificaste la opcion ",a," con la siguiente nota ",n)