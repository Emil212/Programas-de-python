class vehiculos():
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False
    
    def arrancar(self):
        self.enmarcha=True
    
    def acelerar(self):
        self.acelera=True
    
    def frenar(self):
        self.frena=True 

    def estado(self):
        print("Marca:", self.marca, "\nModelo:", self.modelo, "\nEn marcha:", self.enmarcha, "\nAcelerando:", self.acelera, "\nFrenado:", self.frena)



class Furgoneta(vehiculos): #Se hace la herencia

    def carga(self,cargar):
        self.cargado=cargar
        if(self.cargado):
            return "La furgoneta esta cargada"
        else:
            return "La forgoneta no esta cargada"



class Moto(vehiculos):   #Con esto se hace la herencia, se usa pass para hacer pruebas

    hcaballito="" #En las propiedades no se usa el self, y en los metodos si, en el constructor tambien

    def estado(self): #En esta parte se sobreescribe el metodo estado creado en la clase vehiculo
        print("Marca:", self.marca, "\nModelo:", self.modelo, "\nEn marcha:", self.enmarcha, "\nAcelerando:", self.acelera, "\nFrenado:", self.frena, "\n", self.hcaballito)
    def caballito(self):
        self.hcaballito="Voy haciendo el caballito"


class VElectricos(vehiculos):
    def __init__(self, marca, modelo):

        super().__init__(marca, modelo)
        self.autonomia=100
    
    def cargarEnergia(self):
        self.cargando=True


class BicicletaElectrica(VElectricos,vehiculos):    #Herencia multiple, se da preferencia a la primera clase y hereda ese constructor
    pass

    

MiMoto=Moto("Honda", "CBR") #Parametros que se pasan marca & modelo
MiMoto.caballito()
MiMoto.estado() #Se llama el metodo de la clase moto

MiFurgoneta=Furgoneta("Renault", "Kangoo")
MiFurgoneta.arrancar()
MiFurgoneta.estado()
print(MiFurgoneta.carga(True))     #Es el parametro que se envia

MiBici=BicicletaElectrica("Orbes", "IJH")






