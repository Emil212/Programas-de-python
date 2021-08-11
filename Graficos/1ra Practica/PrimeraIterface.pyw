from tkinter import *

raiz=Tk()

raiz.title("ventana de pruebas")

raiz.resizable(1,1)    #Para evitar cambiar el tamaño de la ventana (ancho, alto)

#Para cambiar el icono usar un conversor .ico y colocarlo en la mismacarpeta que el archivo

#para cambiar el icono, t raiz.iconbitmap("Nombre")

#raiz.geometry("650x350") #Para configurar el tamaño de la ventana

raiz.config(bg="white")  #Para cambiar el color del fondo

MiFrame=Frame()  #Con esto se construye el frame 

MiFrame.pack()  #Para empaquetar el frame

#MiFrame.pack(side="left", anchor="n")  #Para empaquetar el frame y al cambiar el tamaño de la raiz el frame se quede en un posicion es especifico
#Left, right, bottom,
#Con achor se puede combinar el lado con un punto cardinal escrito en ingles

#MiFrame.pack(fill="both", expand=True) #Hace que el marco se pueda expander junto con la raiz, x, y, both, none
#fill="y", expand=True hace que se expanda en el eje y 

MiFrame.config(bg="green")

MiFrame.config(width="650", height="350") #El tamaño se le da al frame no directamente a la raiz
#El frame no se puede cambiar de tamaño 

MiFrame.config(bd=35)   #Para agregar borde y cambiarle el tamaño
MiFrame.config(relief="sunken") #Para elegir el tipo de borde

MiFrame.config(cursor="pirate")  #cambia el tipo de cursor que haya en el frame



#Para evitar que al abrir el archivo se abra el interprete cambiar la extension por .pyw
#A la raiz se peude aplicar el borde y cambiar el tipo de raiz

raiz.mainloop() #Siempre al final para que  la interface se esteejecutando todo el tiempo

