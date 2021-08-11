edad=input("Introduce una edad: ")

while(edad.isdigit()==False):   #Verifica que la edad sea un numero
    print("Por favor introduce un valor numerico")
    edad=input("Introduce una edad: ")


if (int(edad)<18):  #Hasta aqui se convierte la edaad en un entero 
    print("No puede pasar")
else:
    print("Puede pasar")

