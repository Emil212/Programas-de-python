#En este programa se utiliza la instruccion super para que se puedan ocupar los atributos de la clase padre
#Esto no ocurre en c++

class Persona():

    def __init__(self, nombre, edad,LugarResidencia):
        self.nombre=nombre
        self.edad=edad
        self.LugarResidencia=LugarResidencia
    
    def descripcion(self):
        print("Nombre:",self.nombre, "\nEdad:", self.edad, "\nResidencia:", self.LugarResidencia)

class Empleado(Persona): #Hereda de la clase persona
    
    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):

        super().__init__(nombre_empleado, edad_empleado, residencia_empleado) #Se utilizan los taributos de la clase padre
        self.salario=salario
        self.antiguedad=antiguedad
    
    def descripcion(self):
        super().descripcion() #Con esta linea se manda a llamar la funcion descripcion de la clase padre
        print("Salario:",self.salario, "\nAntiguedad:",self.antiguedad)

Manuel=Persona("Manuel", 55, "Colombia") 

Manuel.descripcion()

print(isinstance(Manuel, Empleado)) #Para saber si un objeto es de una clase 



#El principio de sustitucion ayuda a saber como se van a manejar las clases
#Por ejemplo un empleado es siempre una persona, pero una persona no es siempre un empledo
#Entonces la clase padre va a ser persona y va a herdar a empleado

