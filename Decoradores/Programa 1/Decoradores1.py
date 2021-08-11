def funcionDecoradora(funcion_parametro):
    
    def funcion_interior():
        
        #Acciones adicionales que decoran

        print("Vamos a realizar un calculo")
        funcion_parametro()

        #Aciones adicionales que decoran

        print("Hemos terminado el calculo")
    
    return funcion_interior


@funcionDecoradora  #Para decorar la funcion suma 
def suma():
    print(15+20)

@funcionDecoradora  #Para decorar la funcion resta  
def resta():
    print(30-10)

suma()
resta()


