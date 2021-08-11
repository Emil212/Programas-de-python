#for i in range(5,50,3): #Permite cambiar la numeracion y el paso 
 #   print(f"valor de la variable {i}") #se ocupapara unir textos y variables con la f no aparecen las llaves al imprimir

valido=False
email=input("Introduce un email: ")
for i in range(len(email)): #Crea un range con la longitud del email
    if email[i]=="@":   #Evalua cada letra del email para ver si hay un arroba
        valido=True
if valido:
    print("Email correcto\n")
else:
    print("Email incorrecto\n")