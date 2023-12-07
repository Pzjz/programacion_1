print("Calculador de pago")

sueldo = float(input("Ingrese el sueldo neto del trabajador: "))


if sueldo<=1000:
    descuento = sueldo*0.10
    sueldo-=descuento
    print("Su sueldo neto es: ",round(sueldo))

elif sueldo>1001 and sueldo<=2000:
    descuento = sueldo*0.05
    sueldo-=descuento
    print("Su sueldo neto es: ",round(sueldo))

else:
    descuento = sueldo*0.03
    sueldo-=descuento
    print("Su sueldo neto es: ",round(sueldo))