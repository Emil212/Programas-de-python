import re 

ListaNombres=['Ana Gomez', 'Maria Martin', 'Sandra Lopez', 'Santiago Martin',]
 
for elemento in ListaNombres:
    if re.findall('^Sandra', elemento): #Con esto mira en cada elemento los que inicien con Sandra
        print(elemento)


for elemento in ListaNombres:
    if re.findall('Martin$', elemento): #Con $ selecciona los elemntos que terminen con la palabra
        print(elemento)

#Puede ser util cuando se desean buscan dominios
#Si se pone entre corchetes busca si en algun lugar se encuentra esa cadena de caracteres

Lista=['hombres', 'mujeres', 'mascotas', 'niños', 'niñas']

for elemento in Lista:
    if re.findall('niñ[oa]s',elemento):
        print(elemento)

ListaCosas=['hombres', 'mujeres', 'mascotas', 'camion', 'camión']

for elemento in ListaCosas:
    if re.findall('cami[oó]n', elemento):
        print(elemento)