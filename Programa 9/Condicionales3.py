salario_presidente=int(input("Introduce el salario del presidente: "))
print("salario presidente: "+ str(salario_presidente)) 

salario_director=int(input("Introduce el salario del director: "))
print("salario director: "+ str(salario_director)) 

salario_jefe_area=int(input("Introduce el salario del jefe de area: "))
print("salario jefe de area: "+ str(salario_jefe_area)) 

salario_administrativo=int(input("Introduce el salario del administrativo: "))
print("salario administrativo "+ str(salario_administrativo)) 

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
    print("Todo funciona correctamente")
else:
    print("Algo esta mal")