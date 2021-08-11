def areaTriangulo(base,altura):

    #"""
   # Calcula el area de un triangulo dado
    #>>> areaTriangulo(3,6)
    #9.0

    #"""

    #return (base*altura)/2
   

    """
    Calcula el area de un triangulo dado 
    >>> areaTriangulo(3,6)
    'El area del triangulo es: 9.0'
    """

    return "El area del triangulo es: " +str((base*altura)/2)

import doctest

doctest.testmod()

#Si no devuelve error es que la funcion esta trabajando correctamente 

#Se puden hacer mas pruebas cambiando los parametros




def CompruebaMail(mailUsuario):

    """
    La funcion evalua un mail recibido en busca de la @.
    Si tiene una @ es correcto, si tiene mas de una es incorrecto.
    Si la @ esta al final es incorrecto

    >>> CompruebaMail('juan@cursor.es')
    True

    >>> CompruebaMail('Juancursos.es@')
    False

    >>> CompruebaMail('Juancursos.es')
    False

    >>> CompruebaMail('Juan@@cursos.es')
    False

    
    """

    arroba=mailUsuario.count('@')

    if(arroba!=1 or mailUsuario.rfind('@') == (len(mailUsuario)-1) or mailUsuario.find('@')==0):
        return False
    
    else:
        return True

import doctest

doctest.testmod()
