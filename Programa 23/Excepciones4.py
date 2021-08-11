import math

def CalculaRaiz(num1):
    if num1<0:
        raise ValueError("El numero no puede ser negativo\n")
    else:
        return math.sqrt(num1)
op1=int(input("Introduce un numero: "))

try:
    print(CalculaRaiz(op1))    
except ValueError as ErrorDeNumeroNegativo: #Con esto se puede cambiar el nombre del error 
    print(ErrorDeNumeroNegativo)

print("Programa Finalizado\n")