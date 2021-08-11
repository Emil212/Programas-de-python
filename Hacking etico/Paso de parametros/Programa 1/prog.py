
import argparse
import sys

"""
parser=argparse.ArgumentParser(description='Paso de parametros')
parser.add_argument("-p1", dest="param1", help="parameter1")
parser.add_argument("-p2", dest="param2", help="parameter2")
params=parser.parse_args()
print(params.param1)
print(params.param2)
"""
"""

parser=argparse.ArgumentParser(description='Process some integers')

parser.add_argument('Integers', metavar='N', type=int, nargs='+', help='An integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum, default=max, help='sum the integers(default:find the max)')
args=parser.parse_args()
print(args.accumulate(args.integers))
"""
"""

print("Numero de argumentos: ", len(sys.argv))
print("Los argumentos son: ", str(sys.argv))

"""




#parser=argparse.ArgumentParser(description='This is a PyMOTW sample')   #Creacion de un parser basico

parser=argparse.ArgumentParser(description='Short sample app')
parser.add_argument('-a', action="store_true", default=False)   #Boleano
parser.add_argument('-b', action="store", dest="b") #Cadena simple
parser.add_argument('-c', action="store", dest="c", type=int)   #Numero entero

#El primer termino es para el nombre 

#dest es para guaardar el valor con un determinado nmbre cuando se analizan los argumentos de la liena de comandos

#Action sive para desencadenar algun tipo de accion 

#Las acciones admitidas incluyen almacenar el argumento individualmente o como parte de una lista...

#...almacenar un valor constante cuando se encuentra un argumento(incluido un manejo para True/False)...

#...contando el numero de eveces que un argumento se ve y se llama a una devolucion de llamada para usar instrucciones de procesaamiento 

print("\n")
print(parser.parse_args(['-a', '-bval', '-c', '3']))    #-bval y -c val sirven para pasar valores a las opciones de un solo caracter
print("\n")

#Lo mismo funciona si son con nombres de opciones mas largos

parser1=argparse.ArgumentParser(description='Example with long option names') 
parser1.add_argument('--noarg', action="store_true", default=False)
parser1.add_argument('--witharg', action="store", dest="witharg")
parser1.add_argument('--witharg2', action="store", dest="witharg2",type=int)

print(parser1.parse_args(['--noarg', '--witharg', 'val', '--witharg2=3']))
print("\n")

#argparse es una herramienta completa de analisis de argumentos de linea de comandos y maneja argumentos opcionales y requeridos

parser2=argparse.ArgumentParser(description='Example with nonptional arguments')
parser2.add_argument('count', action="store", type=int)
parser2.add_argument('units', action="store")

print(parser2.parse_args())

