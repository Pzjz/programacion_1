print("===============================================================")
print("===============================================================")
print("                      Calculador de IMC")
print("===============================================================")

peso = int(input("Ingrese su peso: "))
altura = float(input("Ingrese su estatura recuerda ponerlo en decimal: "))

resultado = peso/altura**2

print("El indice de masa corporal(IMC) es: ",round(resultado,1))