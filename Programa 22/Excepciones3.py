def EvaluarEdad(Edad): #En el caso del if y el elif evalua la primera condicion, si es verdadera se queda ahi si no avanza a la que sigue
    if Edad <0:
        raise TypeError("No se permiten edades negativas\n") #Aqui se crea nuestra propia excepcion y se puede utilizar el nombre que sea par5a la excepcion
    
    if Edad<20:
        return "Eres muy joven\n"
    elif Edad<40:
        return "Eres joven\n"
    elif Edad<65:
        return "Eres maduro\n"
    elif Edad<100:
        return "Cuidate mucho porfa <3\n"

print(EvaluarEdad(15))