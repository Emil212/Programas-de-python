import pickle

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


coche1=vehiculos("Mazda", "MX5")
coche2=vehiculos("Seat", "Leon")
coche3=vehiculos("Renault", "Megane")

choches=[coche1, coche2, coche3]

fichero=open("LosCoches", "wb")

pickle.dump(choches, fichero)

fichero.close()

del (fichero)

ficheroApertura=open("LosCoches", "rb")

MisCoches=pickle.load(ficheroApertura)

ficheroApertura.close()

for i in MisCoches:
    print(i.estado())