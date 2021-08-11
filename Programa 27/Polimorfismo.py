class Coche():

    def desplazamiento(self):
        print("\nMe desplazo utilizando cuatro ruedas\n")

class Moto():

    def desplazamiento(self):
        print("\nMe desplazo utilizando dos ruedas\n")

class Camion():
    
    def desplazamiento(self):
        print("\nMe desplazo utilizando seis ruedas\n")


def DesplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()

MiVehiculo=Moto()
DesplazamientoVehiculo(MiVehiculo) #Al pasar por parametro vehiculo transforma al objeto en un objeto tipo camion