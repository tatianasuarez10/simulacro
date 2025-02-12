suma = 0
contador = 0

while contador < 12 :
    domicilio = int(input("ingrese la distancia recorrida de 12 servivios de domicilio "))
    if domicilio <= 5:
            print("el numero no es valido ")
            continue
    print("el numero es valido ")
    suma += domicilio
    contador += 1
else:
    print("nein es posible")


contaminacion = suma*43/12
print(f"el promdio de contaminacion es {contaminacion}")
print(f"estos son los kilometros recorridos {suma}")
