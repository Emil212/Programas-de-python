class Coche():
    def __init__(self): #Este es el constructor asgina el estado inicial de las propiedades
        
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4 #Con esto se puede encapsular una propiedad para que no sea accesiblie fuera de la clase
        self.__enmarcha=False

    def arrancar(self,arrancamos):
        self.__enmarcha=arrancamos
        if(self.__enmarcha):
            chequeo=self.__ChequeoInterno() #Para encapsular el metodo y no se puede acceder fuere de la clase 
        if(self.__enmarcha and chequeo):    #Al no poner nada se considera que es True
            return "El coche esta en marcha"
        elif(self.__enmarcha and chequeo==False):
            return "Algo ha ido mal en el chequeo. No se puede arancar"
        else:
            return "El coche esta parado"

        

    def estado(self):
        print("El coche tiene: ")
        print(self.__ruedas, " ruedas")
        print("Un ancho de ",self.__anchoChasis)
        print("Un largo de ", self.__largoChasis)
        
    def __ChequeoInterno(self):
        print("Realizando chequeo interno")
        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"

        if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False 

MiCoche=Coche() #Instanciar una clase 
print(MiCoche.arrancar(True))
MiCoche.estado()


print("A continuacion crearemos el segundo objeto\n")

MiCoche2=Coche()
print(MiCoche2.arrancar(False))
MiCoche2.estado()

