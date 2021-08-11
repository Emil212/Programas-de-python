#Crear un programa que pide numeros positivos indefinidamente, el programa termina si se introduce uno negativo y al final muestre la suma
acomulador=0
numero=int(input("Ingrese un numero positivo: "))

if numero>=0:
    while numero>=0:
        acomulador=acomulador+numero
        numero=int(input("Ingrese un numero positivo: "))
      
    print("La suma es: " + str(acomulador))
    print("Fin del programa")

else:
    print("El numero es negativo. Fin del programa\n")
