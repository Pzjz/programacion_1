print("Calculador de precio de moto por dia")
print("martes descuento de 12%")
print("sabado descuento de 18%")
print("domingo descuento de 25%")
print("La moto cuesta 20000")
 
dia = input("Ingresa el dia(Buena ortografia): ")

if dia == "martes":
    descuento = 20000*0.12
    descuento = 20000 - descuento
    print("El precio de la moto en el dia martes es de: ",round(descuento))
elif dia == "sabado":
    descuento = 20000*0.18
    descuento = 20000 - descuento
    print("El precio de la moto en el dia sabado es de: ",round(descuento))
elif dia == "domingo":
    descuento = 20000*0.25
    descuento = 20000 - descuento
    print("El precio de la moto en el dia domingo y feriado es de: ",round(descuento))
