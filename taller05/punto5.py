print("Total a pagar por las prendas!!")
print("Costo de la camisa 10000")
print("Si realizo una compra con un total de 3 o mas camisas tiene un descuento del 20% si son menos un descuento del 10%")
a = int(input("Ingrese el total de camisas que adquirio: "))

if a>=3:
    a*=10000
    b= a*0.20
    a-=b
    print("El total de la compra con el descuento de 20% es de: ",round(a))
else:
    a*=10000
    b= a*0.10
    a-=b
    print("El total de la compra con el descuento de 10% es de: ",round(a))