from tkinter import *

raiz=Tk()

MiFrame=Frame(raiz)

MiFrame.pack()

operacion=""

resultado=0

#****************************PANTALLA*******************************************
numeroPantalla=StringVar()


pantalla=Entry(MiFrame, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(bg="black", fg="#03f943", justify="right")

#****************************PULSACIONES TECLADO*******************************

def NumeroPulsado(num): #Este num es solo para que en pantalla aparezca lo que estamos teclando
    global operacion

    if operacion!="":

        numeroPantalla.set(num)     #Para no concatenar
        operacion=""    #Para que vuelva a concatenar 
    
    else:
        numeroPantalla.set(numeroPantalla.get()+num)    #Para que al pulsar varias veces aparezcan mas numeros


#***************************FUNCION SUMA***************************************

def suma(num):  #Numero para hacer la suma
    global operacion
    global resultado
    resultado+=int(num)
    operacion="suma"
    numeroPantalla.set(resultado)

#**************************FUNCION RESULTADO*********************************

def resta(num):
    global resultado
    global operacion

    
    resultado=resultado-int(num)
    operacion="resta"
    numeroPantalla.set(resultado)

#*************************FUNCION EL RESULTADO*******************************

def ElResultado():
    global resultado

    numeroPantalla.set(resultado+int(numeroPantalla.get())) #con set se muestra en pantalla, y con get se toma lo que esta en pantalla
    #En este caso el numero que se va a mostar en pantalla va a ser lo que este almacenado en la variable resultado
    #Mas lo que esye en la pantalla en ese momento
    resultado=0

#***************************FILA 1*********************************************

boton7=Button(MiFrame, text="7", width=3, command=lambda:NumeroPulsado("7"))   
boton7.grid(row=2, column=1)
boton8=Button(MiFrame, text="8", width=3, command=lambda:NumeroPulsado("8"))
boton8.grid(row=2, column=2)
boton9=Button(MiFrame, text="9", width=3, command=lambda:NumeroPulsado("9"))
boton9.grid(row=2, column=3)
botonDiv=Button(MiFrame, text="/", width=3)
botonDiv.grid(row=2, column=4)


#***************************FILA 2*********************************************

boton4=Button(MiFrame, text="4", width=3, command=lambda:NumeroPulsado("4"))   
boton4.grid(row=3, column=1)
boton5=Button(MiFrame, text="5", width=3, command=lambda:NumeroPulsado("5"))
boton5.grid(row=3, column=2)
boton6=Button(MiFrame, text="6", width=3, command=lambda:NumeroPulsado("6"))
boton6.grid(row=3, column=3)
botonMul=Button(MiFrame, text="*", width=3)
botonMul.grid(row=3, column=4)


#***************************FILA 3*********************************************

boton1=Button(MiFrame, text="1", width=3, command=lambda:NumeroPulsado("1"))   
boton1.grid(row=4, column=1)
boton2=Button(MiFrame, text="2", width=3, command=lambda:NumeroPulsado("2"))
boton2.grid(row=4, column=2)
boton3=Button(MiFrame, text="3", width=3, command=lambda:NumeroPulsado("3"))
boton3.grid(row=4, column=3)
botonRes=Button(MiFrame, text="-", width=3, command=lambda:resta(numeroPantalla.get()))
botonRes.grid(row=4, column=4)


#***************************FILA 4*********************************************

boton0=Button(MiFrame, text="0", width=3, command=lambda:NumeroPulsado("0"))   
boton0.grid(row=5, column=1)
botonComa=Button(MiFrame, text=",", width=3, command=lambda:NumeroPulsado(","))
botonComa.grid(row=5, column=2)
botonIgual=Button(MiFrame, text="=", width=3, command=lambda:ElResultado())
botonIgual.grid(row=5, column=3)
botonSum=Button(MiFrame, text="+", width=3, command=lambda:suma(numeroPantalla.get()))    #Para mandar el numero que este en la pantalla
botonSum.grid(row=5, column=4)







raiz.mainloop()