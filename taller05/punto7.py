print("Calculador de promedio de alumno con la calificacion")

n1 = float(input("Ingrese la primera nota: "))
n2 = float(input("Ingrese la segunda nota: "))
n3 = float(input("Ingrese la tercera nota: "))
n4 = float(input("Ingrese la cuarta nota: "))
n5 = float(input("Ingrese la quinta nota: "))
promedio = (n1+n2+n3+n4+n5)/5

if promedio>=3:
    print("El promedio del estudiante es: ",promedio," El estudiante aprobo")

else:
    print("El estudiante reprobo con un:",promedio)
