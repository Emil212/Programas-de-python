#Crear un programa que pida introducir una contraseña. lo podra tener menos de 8 caracteris, ni espacios en blanco

contraseña=input("Ingrese una contraseña: ")
contador=0

for i in range(len(contraseña)):
    if len(contraseña)<7:
        contador=contador+1
    if contraseña[i]==" ":
        contador=contador+1
 
if contador==0:
     print("Contraseña correcta\n")
else:
    print("Conatraseña incorrecta\n")