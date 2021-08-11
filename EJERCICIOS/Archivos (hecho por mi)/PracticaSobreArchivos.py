import pickle
import os

#Definicion de la clase persona

class Persona():

    def __init__(self, nombre, apellido_pat,apellido_mat, genero, edad):
        self.nombre=nombre
        self.apellido_pat=apellido_pat
        self.apellido_mat=apellido_mat
        self.genero=genero
        self.edad=edad   
    
   
    def LeerPersona(self):
        
        self.nombre=input("Nombre: ")
        while (self.nombre.isalpha()==False):
            print("NOMBRE INVALIDO. INGRESELO DE NUEVO")
            self.nombre=input("Nombre: ")

        self.apellido_pat=input("Apellido paterno: ")
        while (self.apellido_pat.isalpha()==False):
            print("APELLIDO INVALIDO. INGRESELO DE NUEVO")
            self.apellido_pat=input("Apellido paterno: ")
        
        self.apellido_mat=input("Apellido materno: ")
        while(self.apellido_mat.isalpha()==False):
            print("APELLIDO INVALIDO. INGRESELO DE NUEVO")
            self.apellido_pat=input("Apellido Materno: ")

        self.genero=input("Genero: ")
        while(self.genero.isalpha()==False):
            print("GENERO INVALIDO. INGRESELO DE NUEVO")
            self.apellido_pat=input("Genero: ")

        self.edad=input("Edad: ")
        while(self.edad.isdigit()==False):
            print("EDAD INVALIDA. INGRESELA DE NUEVO")
            self.apellido_pat=input("Edad: ")
    
    
    def ImprimirPersona(self):
        print("Nombre:", self.nombre.upper(), self.apellido_pat.upper(), self.apellido_mat.upper(), "\nGenero:", self.genero.upper(), "\nEdad", self.edad)


#Definicion de la clase Empleado

class Empleado(Persona): #Va a heredar de la clase persona
    
    def __init__(self, puesto="", salario="", antiguedad="", nombre_empleado="", apellidopat_empleado= "", apellidomat_empleado="" , genero_empleado="", edad_empleado=""):
        super().__init__(nombre_empleado, genero_empleado, edad_empleado, apellidopat_empleado , apellidomat_empleado) #Con esto se utilizan los atributos de la clase padre (Persona)
        self.puesto=puesto
        self.salario=salario
        self.antiguedad=antiguedad
    
    def LeerEmpleado(self):
        super().LeerPersona()

        self.puesto=input("Puesto: ")
        while(self.puesto.isalpha()==False):
            print("PUESTO INVALIDO. INGRESELO DE NUEVO")
            self.puesto=input("Puesto: ")

        self.salario=input("Salario: ")
        while(self.salario.isdigit()==False):
            print("SALARIO INVALIDO. INGRESELO DE NUEVO")
            self.salario=input("Salario: ")

        self.antiguedad=input("Antiguedad: ")
    
    def ImprimirEmpleado(self):
        super().ImprimirPersona()
        print("Puesto:", self.puesto.upper(), "\nSalario:", self.salario, "\nAntiguedad:", self.antiguedad)



class Lista:
    
    Personas=[]

    def __init__(self):
        ListaDePersonas=open("Control", "ab+")
        ListaDePersonas.seek(0)

        try:
            self.Personas=pickle.load(ListaDePersonas)
            print("Se cargaron {} personas".format(len(self.Personas)))
        except:
            print("La lista se encuentra vacia")
        finally:
            ListaDePersonas.close()
            del (ListaDePersonas)

    def Agregar(self,p):
        self.Personas.append(p)
        
    
    def ImprimirLista(self):
        for p in self.Personas:
            print(p)
    
    def Guardar(self):
        Lista=open("Control", "wb")
        pickle.dump(self.Personas, Lista)    
        del(Lista)

os.system("cls")

MiLista=Lista()
emp=Empleado()
opcion= 0

while opcion!=4:
    print("Bienvenido a la lista\n ")
    print("1.- AGREGAR EMPLEADO")
    print("2.- IMPRIMIR LISTA")
    print("3.- RECUPERAR INFORMACION")
    print("4.- SALIR")

    opcion=int(input("Favor de seleccionar una opcion: "))
    
    if opcion==1:
        os.system("cls")
        emp.LeerEmpleado()
        MiLista.Agregar(emp)
        MiLista.Guardar()
        print("Se ha agregado correctamente el empleado\n")
        os.system("pause")
        os.system("cls")

    elif opcion==2:
        os.system("cls")
        
        if(emp.nombre!=""):
            
            MiLista.ImprimirLista()
        
        else:
            print("LISTA VACIA\n")

        os.system("pause")
        os.system("cls")
    
    elif opcion==3:
        os.system("cls")


os.system("cls")



    