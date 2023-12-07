print("El costo de la matricula es 10000")
n1= float(input("Ingresa la primera nota del estudiante: "))
n2= float(input("Ingresa la segunda nota del estudiante: "))
n3= float(input("Ingresa la tercera nota del estudiante: "))
n4= float(input("Ingresa la cuarta nota del estudiante: "))
prom = 0
prom = n1+n2+n3+n4
prom /=4

if prom >= 4 and prom <=5:
    print("Su promedio es excelente y tiene descuento del 20% en la matricula su matricula tendra un valor de 2000")
elif prom >= 3 and prom<=3.99:
    print("Su promedio es Bueno pero no aplica descuento")
elif prom >= 0 and prom<=2.99:
    print("Su promedio es deficiente y no aplica descuento")
else:
    print("Error")