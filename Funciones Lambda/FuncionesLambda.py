area_triangulo=lambda base, altura: (base*altura)/2

print(area_triangulo(7,5))

print(area_triangulo(7,6))


al_cubo=lambda numero:pow(numero,3)

print(al_cubo(13))

destacar_valor=lambda comision: "¡{}$!".format(comision)

comision_Ana=155000
print(destacar_valor(comision_Ana))