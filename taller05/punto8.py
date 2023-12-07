print("======================================")
print("======================================")
print("Bienvenido a nuestra tienda de motos")
print("======================================")
print("Contamos con promociones de final de año")
print("yamaha: $20000 con descuento del 8%")
print("honda: $10000 con descuento del 5%")
print("suzuki: $15000 con descuento del 10%")
print("otras: $8000 con descuento del 2%")
user = input("Escoje la moto(Buena ortografia): ")

if user == "yamaha":
    precioFinal= 20000*0.08
    precioFinal= 20000 - precioFinal
    print("El precio de la moto yamaha: ",round(precioFinal))
elif user == "honda":
    precioFinal= 10000*0.05
    precioFinal= 10000 - precioFinal
    print("El precio de la moto honda: ",round(precioFinal))
elif user == "suzuki":
    precioFinal= 15000*0.10
    precioFinal= 15000 - precioFinal
    print("El precio de la moto suzuki: ",round(precioFinal))
elif user == "otras":
    precioFinal= 8000*0.02
    precioFinal= 8000 - precioFinal
    print("El precio de la moto otras: ",round(precioFinal))