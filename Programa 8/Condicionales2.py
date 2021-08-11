print("verificacion de nota")

nota_alumno=float(input("Ingrese su nota: "))

if nota_alumno<6:
      print("Insuficiente\n")
      
elif nota_alumno<7 and nota_alumno >=6:
     print("Suficiente\n")

elif nota_alumno<8 and nota_alumno >=7:
     print("Bien\n")
     
elif nota_alumno<9 and nota_alumno>= 8:
     print("notable9\n")

elif nota_alumno<10 and nota_alumno>=9:
     print("sobresaliente\n")
     
elif nota_alumno==10:
     print("Excelente\n")

else:
     print("Verificar calificacion\n")
     
print("El programa ha finalizado\n")
