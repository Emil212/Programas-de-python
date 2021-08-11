#Programa que pide numeros infinitamente, los numero seran cada vez mayores y si se introduce uno menor que el anterio finaliza

numero_ant=int(input("Introduce un numero: "))
numero_nuevo=int(input("Introduce un numero mayor que " + str(numero_ant) + ": "))

while numero_nuevo>numero_ant:
    numero_ant=numero_nuevo
    numero_nuevo=int(input("Introduce un numero mayor que " + str(numero_ant) + ": "))

print("Ingresaste un numero menor que el anterior. Fin del programa\n")

    