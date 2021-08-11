#Crear un programa que al introducir un email diga si es correcto o incorrecto

email=input("Introduce un email: ")

arroba=email.count('@')

if (arroba!=1 or email.rfind('@')==(len(email)-1) or email.find('@')==0 ):
    print("Email incorrecto\n")

else:
    print("Email correcto\n")