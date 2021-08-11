import re

cadena="Vamos a aprender expresiones regulares en Python. Python es un lenguaje de sintaxis sencilla"

#print(re.search("aprender",cadena)) #devuelve un objeto si encuentra en texto o un none si no lo encuentra

#textoBuscar="aprender"

"""if re.search(textoBuscar, cadena) is not None:  #Puede ser util para las BBDD?
    print("He encontrado el texto")

else:
    print("No he encontrado el texto")"""

#textoEncontrado=re.search(textoBuscar,cadena)

#print(textoEncontrado.start())  #El numero de caracter donde empieza a encontrar el texto
#print(textoEncontrado.end())    #El numero de caracter donde se acaba el texto 
#print(textoEncontrado.span())   #Hace lo mismo que star y end pero en una sola funcion ademas de que lo guarda en una tupla


TextoBuscar="Python"

print(len(re.findall(TextoBuscar, cadena)))  #Busca los textos especificados dentro de una cadena y en una tupla regresa los textos