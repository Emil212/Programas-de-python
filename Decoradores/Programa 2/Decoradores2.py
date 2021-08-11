def funcionDecoradora(funcion_parametro):
    
    def funcion_interior(*args, **kwargs):    #Puede recibir un numero indeterminado de parametros, keyword
        
        #Acciones adicionales que decoran

        print("Vamos a realizar un calculo:")
        funcion_parametro(*args, **kwargs)

        #Aciones adicionales que decoran

        print("Hemos terminado el calculo")
    
    return funcion_interior


@funcionDecoradora  #Para decorar la funcion suma 
def suma(num1,num2,num3):
    print(num1+num2+num3)

@funcionDecoradora  #Para decorar la funcion resta  
def resta(num1,num2):
    print(num1-num2)

@funcionDecoradora
def potencia(base, exponente):
    print(pow(base,exponente))


suma(7,5,8)
resta(12,10)
potencia(base=5, exponente=3)
