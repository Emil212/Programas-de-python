class Empleado:

    def __init__(self, nombre, cargo, salario):
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario
    
    def __str__(self):
        return "{} que trabaja como {} tiene in salario de {}$".format(self.nombre, self.cargo, self.salario)


ListaEmpleados=[

Empleado("Juan", "Director", 7500),
Empleado("Ana", "Presidente", 8500),
Empleado("Antonio", "Administrativo", 2500),
Empleado("Sara", "Secretariar", 2700),
Empleado("Mario", "Botones", 2100)
]
    
def calculo_comision(empleado):
    if(empleado.salario<=3000):
        empleado.salario=empleado.salario*1.03
    return empleado

ListaEmpleadosComision=map(calculo_comision, ListaEmpleados)

for empleado in ListaEmpleadosComision:
    print(empleado)
