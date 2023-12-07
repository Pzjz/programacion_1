print("================================================================")
print("================================================================")
print("Bienvenido a nuestra empresa telefonica")
print("Opcion1-------->Estados unidos: 900 por minuto")
print("Opcion2-------->Canada: 800 por minuto")
print("Opcion3-------->Europa: 950 por minuto")
print("Opcion4-------->Resto del mundo: 1250 por minuto")
print("Si la llamada supera los 15 minutos tienes un descuento del 20%")

llamada = int(input("Entre las opciones elige: "))
duracion = int(input("Ingrese tiempo de llamada: "))
total = 0
a=0
if llamada == 1:
    total = 900*duracion
elif llamada ==2:
    total = 800*duracion
elif llamada ==3:
    total = 950*duracion
elif llamada ==4:
    total = 1250*duracion

if duracion>= 15:
    a=total*20/100
    total-=a
    print("El total a pagar con el descuento es de: ",round(total))
else:
    print("No aplica descuento el tal a pagar por la llamada es: ",total)