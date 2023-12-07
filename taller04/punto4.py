
n1 = float(input("Ingrese primera nota,Taller 1: 20%-----> "))
n2 = float(input("Ingrese segunda nota,Taller 2: 15%------>  "))
n3 = float(input("Ingrese tercera nota,Cuestionario 1: 22%-----> "))
n4 = float(input("Ingrese cuarta nota,Cuestionario 2: 10%------> "))
n5 = float(input("Ingrese quinta nota, Proyecto final: 33%-----> "))
prom = 0

n1 = (n1*20)/100
n2 = (n2*15)/100
n3 = (n3*22)/100
n4 = (n4*10)/100
n5 = (n5*33)/100

prom = n1+n2+n3+n4+n5
print("La nota definitiva es: ",round(prom,1))