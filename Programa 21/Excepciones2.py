def divide():
    try:
        op1=float(input("Introduce el primer numero: "))
        op2=float(input("Introduce el segundo numero: "))
        print("La division es es: " + str(op1/op2))
    except ValueError:  #Se puede manejar una excepcion general pero no es del todo recomendable, porque el usuario no entiende que fue lo que fallo
        print("El valor introducido es erroneo\n")
    except ZeroDivisionError:
        print("No se puede dividir entre 0\n")
    finally:    #Siempre se ejecuta lo que esta dentro del finally y tambien se puede ocupar solo el finally sin el except pero no olvidar el try
        print("Calculo finializado\n")

divide()
