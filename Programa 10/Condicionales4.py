print("Asignaturas optativas\n")
print("Informatica Grafica - Pruebas de Software - Usabilidad y Accesibilidad\n")
opcion=input("Escribe la asignatura escogida: ")
Asignatura=opcion.lower() #lower y upper convierten toda la oracion a minusculas y mayusculas respectivamente
if Asignatura in("informatica grafica", "pruebas de software", "usabilidad y accesibilidad"):
    print("Asignatura elegida: " + Asignatura) #No se opcupa str para cogcatear
else:
    print("verificar la asignatura\n")