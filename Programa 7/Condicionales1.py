print("Programa de evaluacion de notas de alumnos") #Cualquier cosa introducida a python es un valor numerico 

nota_alumno=input()

def evaluacion(nota_alumno):
     valoracion="aprobado"
     if nota_alumno<=5:
          valoracion="reprobado"
     return valoracion

print(evaluacion(int(nota_alumno))) #El int convierte el valor string a un numero entero
