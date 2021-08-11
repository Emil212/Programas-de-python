import math
print("PROGRAMA QUE CALCULA LA RAIZ CUADRDA")
numero=int(input("Introduce un numero: "))
intentos=0

while numero<0:
    print("La raiz de un numero negativo es compleja\n")
    
    if intentos==2:
        print("Haz consumido demasiados intentos. El progrma ha finalizado\n")
        break;
    
    numero=int(input("Introduce un numero: "))
    if numero<0:
        intentos=intentos+1

if intentos<2:
    solucion=math.sqrt(numero)
    print("La raiz cuadrada de " + str(numero) + " es: "  + str(solucion))
    
