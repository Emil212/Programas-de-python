contador=0
Direccion=input("introduzca una direccion de correo: ")
for i in Direccion:
    if(i=="@" or i=="."):
        contador=contador+1
if contador>=2: #Se puede omnitir el ==True ya que por defecto la considera verdadera
    print("Email correcto\n")
else:
    print("verificar email\n")


#Con range(i) crea una lista con i elementos, range es un tipo de dato y se puede ocupar para el for