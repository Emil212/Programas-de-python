import pickle

class Persona:
    def __init__(self, nombre, genero, edad):   #Constructor
        self.nombre=nombre
        self.genero=genero
        self. edad=edad
        print("Se ha creado una persona nueva con el nombre de", self.nombre)
    
    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)
    
class ListaPersonas:

    Personas=[]

    def __init__(self):
        ListaDePersonas=open("FicheroExterno", "ab+")   #Abre el archivo en append
        ListaDePersonas.seek(0) #Para colocar el puntero al inicio
        

        try:
            self.Personas=pickle.load(ListaDePersonas)
            print("Se cargaron {} personas del fichero externo".format(len(self.Personas)))
        
        except:
            print("El fichero esta vacio")
        
        finally:
            ListaDePersonas.close()
            del (ListaDePersonas)

    def AgregarPeronas(self,p): #No importa el nombre de la segunda variable
        self.Personas.append(p)
        self.GuardarPersonas()

    def MostarPersonas(self):
        for p in self.Personas:
            print(p)
    
    def GuardarPersonas(self):
        ListaPersonas=open("FicheroExterno", "wb")
        pickle.dump(self.Personas, ListaPersonas)   #El primer parametro es la variable a guardar y el segundo a donde se va a guardar
        del (ListaPersonas)
    
    def MostrarInfoFicheroExterno(self):
        print("La informacion del fichero externo es la siguiente")
        for p in self.Personas:
            print(p)



MiLista=ListaPersonas()

persona=Persona("Ana", "Femenino", 19)
MiLista.AgregarPeronas(persona)
MiLista.MostrarInfoFicheroExterno()
