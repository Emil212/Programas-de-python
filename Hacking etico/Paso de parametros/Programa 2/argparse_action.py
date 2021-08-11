"""
Cualquiera de las seis acciones integraadas se puede activar cuando un argumento es encontrado

store: Guarda el valordespues de convertirlo opcionalmente a un tipo diferente.
Esta es la accion predeterminada que se toma si no se especifica ninguna explicitamente

store_const: Guarda un valor definido como parte de la especificacion del argumento, en lugar del valor
que proviene de los argumentos que se analizan. Esto normalmente se usa para implantar banderas de linea
de comandos que no son booleanos

store_true/store_false: Guarda el valor booleano apropiado. Estas acciones se utilizan para implementar 
interruptores booleanos

append: Guarda el valor en una lista, Se guaradn varios valores si el argumento se repite

append_const: Guarda un valor definido en la especificacion del argumento en una lista

version: Imprime detalles de la version sobre el programa y luego sale 


ESTE PROGRAMA DE EJEMPLO MUESTRA CADA TIPO DE ACCCION, CON LA MINIMA CONFIGURACION
"""

import argparse

parser=argparse.ArgumentParser()

parser.add_argument('-s', action='store', dest='simple_value', help='Store simple value')
parser.add_argument('-c', action='store_const', dest='const_value', const='value-to-store', help='Store a constant value')
parser.add_argument('-t', action='store_true', default=False, dest='boolean_t', help='Set a switch to true')
parser.add_argument('-f', action='store_false', default=True, dest='boolean_f', help='Set a switch to false')
parser.add_argument('-a', action='append', dest='collection', default=[], help='Add repeated values to a list')
parser.add_argument('-A', action='append_const', dest='const_collection', const='value-1-to-append', default=[], help='Add different values to list' )
parser.add_argument('-B', action='append_const', dest='const_collection', const='value-2-to-append', help='Add different values to list')
parser.add_argument('--version', action='version', version='%(prog)s 1.0')

results=parser.parse_args()
print('simple_value         = {!r}'.format(results.simple_value))
print('constant_value       = {!r}'.format(results.const_value))
print('boolean_t            = {!r}'.format(results.boolean_t))
print('boolean_f            = {!r}'.format(results.boolean_f))
print('collection           = {!r}'.format(results.collection))
print('const_collection     = {!r}'.format(results.const_collection))







