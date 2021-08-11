#Nota el juego no funciona de la manera edecuada

import random
import os

digitos=("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
codigo=""

for i in range(4):
    candidato=random.choice(digitos)

    while candidato in codigo:
         candidato=random.choice(digitos)
    
    codigo=codigo+candidato



print("BIENVENIDO AL JUEGO\n")

print("Intrucciones: Tienes que encontrar un numero de 4 cifras\n")

propuesta=input("¿Cual es tu primera propuesta?: ")

intentos=1

while propuesta!=codigo:
    intentos=intentos+1
    aciertos=0
    coincidencias=0

    for i in range(4):
        if propuesta[i]==codigo[i]:
            aciertos=aciertos+1

        elif propuesta[i] in codigo:
            coincidencias=coincidencias+1
        
        print(codigo)
        print("Tu propuesta", propuesta, "tiene:", aciertos, "Aciertos", coincidencias, "Coincidencias")
       
        propuesta=input("Ingresa otra propuesta: ")
        

print("FELICITACIONES\n Adivinaste el codigo en", intentos, "intentos")
        




