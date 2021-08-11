def DevuelveCiudades(*Ciudades):    #Con * se indica que va a recibir un numero indeterminqado de elementos, en forma de tupla
    for elemento in Ciudades:
        #for subelemento in elemento:
            yield from elemento #Es el mismo resultado que usar bucles anidados y asi se obtienen los subelementos


CiudadesDevueltas=DevuelveCiudades("Madrid", "Barcelona", "Bilbao", "Valencia")
print(next(CiudadesDevueltas))
print(next(CiudadesDevueltas))