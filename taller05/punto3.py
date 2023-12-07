print("Programa que determina el menor numero de 3 numero y su respectiva suma")

num1 = int(input("Ingrese el primer valor: "))
num2 = int(input("Ingrese el segundo valor: "))
num3 = int(input("Ingrese el tercer valor: "))
menor = 0
r=0
if num1<num2 and num1<num3:
    menor=num1
elif num2<num1 and num2<num3:
    menor=num2
else:
    menor=num3

r=num3+num2+num1

print("El numero menor de los 3 es: ",menor," y su sumatoria seria de: ",r)