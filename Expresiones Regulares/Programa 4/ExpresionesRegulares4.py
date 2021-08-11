import re

nombre1="Sandra Lopez"
nombre2="Antonio Gomez"
nombre3="Lara Lopez"
nombre4="Jara Suarez"
cadena1="Jara Lopez"
cadena2="454545454"
cadena3="a45454678"
#Match busca si hay coincidencias en una cadena de texto al comienzo, distingue mayusculas y minusculas 

if re.match("Sandra", nombre1, re.IGNORECASE):  #Para deshabilitar el sensitive case
    print("Hemos encintrado el nombre")

else:
    print("No lo hemos encontrado")


if re.match(".ara", nombre3, re.IGNORECASE):  #El . es para ignorar la primera letra y solo busca en la terminacion
    print("Hemos encintrado el nombre")

else:
    print("No lo hemos encontrado")



if re.match("\d", cadena1):  #\d sirve para detectar si una cadena comienza con digitos 
    print("Hemos encintrado el numero")

else:
    print("No lo hemos encontrado")


if re.search("Lopez", nombre3, re.IGNORECASE):  
    print("Hemos encintrado el nombre")

else:
    print("No lo hemos encontrado")

#Search busca en toda la cedena de texto un patron de busqueda 