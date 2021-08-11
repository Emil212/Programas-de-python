edad=int(input("Introduce una edad: "))
while edad>5 or edad>100:   #Se pueden concatenar condiciones al igual que en if 
    print("Edad erronea. Favor de verificar\n")
    edad=int(input("Introduce una edad: "))
print("Gracias")
print("Edad: "+ str(edad))
