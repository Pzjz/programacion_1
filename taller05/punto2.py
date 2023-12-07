print("Programa que determina el mayor numero de 3 numeros")

num1 = int(input("Ingrese el primer valor: "))
num2 = int(input("Ingrese el segundo valor: "))
num3 = int(input("Ingrese el tercer valor: "))
mayor = 0
if num2<num1>num3:
    mayor = num1
    print(mayor)
elif num1<num2>num3:
    mayor = num2
    print(mayor)
elif num1<num3>num2:
    mayor = num3
    print(mayor)