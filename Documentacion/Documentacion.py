class Areas:

    def AreaCuadrado(lado):

        """Calcula el area de un cuadrado elevando al cuadrado el lado pasado por parametro"""
    
        return "El area del cuadrado es: " + str(lado*lado)


    def AreaTriangulo(base,altura):

        """Calcula el area de un triangulo pasado por parametro el la base y la altura"""
    
        return "El area del triangulo es: " + str((base*altura)/2)




#print(AreaCuadrado(3))
#print(AreaCuadrado.__doc__) #Para imprimir la documentacion asociada a la funcion 

#help(AreaCuadrado)  #Igual sirve para imprimir la documentacion 

help(Areas)    #Cuando la funcion pertenece a una clase


