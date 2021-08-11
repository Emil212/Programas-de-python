def GeneraPares(limite):
    num=1

    while num<limite:
        yield num*2
        num=num+1

DevuelvePares=GeneraPares(10)
  
print(next(DevuelvePares))  #Sirve para imprimir uno a uno los elementos , no se crea toda la lista desde el principio

print("Mas codigo")

print(next(DevuelvePares))  #

print("Mas codigo")

print(next(DevuelvePares))