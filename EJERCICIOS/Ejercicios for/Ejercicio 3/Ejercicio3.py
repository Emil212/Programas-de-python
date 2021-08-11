#Crear un programa que evalue si una direcion de correo es valida o no en funcion si tiene "@". y su tine un punto o mas
contador1=0
contador2=0
correo=input("Ingrese un correo electronico: ")

for i in range(len(correo)):
    if correo[i]=="@":
        contador1=contador1+1
    if correo[i]==".":
        contador2=contador2+1

if contador1==1 and contador2!=0:
    print("Correo valido\n")
else:
    print("Correo invalido\n")
