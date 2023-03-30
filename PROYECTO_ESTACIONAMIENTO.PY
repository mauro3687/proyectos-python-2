from cProfile import label
from cgitb import text
from ctypes.wintypes import SIZE
from difflib import HtmlDiff
from distutils.cmd import Command
from distutils.command.config import config
from logging import root
from lzma import MODE_NORMAL
from msilib.schema import Font
from pickle import FRAME
from re import M, T
from shutil import register_archive_format
from sqlite3 import sqlite_version
from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD
from traceback import format_tb
from tkinter import messagebox
from PIL import ImageTk,Image
from tkinter import messagebox as mb			
import tkinter as tk
import sqlite3
color='#c5e2f6'			#Codigo HEX del color de fondo usado
		

def Menu():
    global pantalla
    pantalla=Tk()
    pantalla.geometry("400x550")
    pantalla.title("ESTACIONAMIENTO")
    pantalla.config(bg="#C8A2C8")
    pantalla.iconbitmap("icono.ico")
    etiquet=Label(pantalla,text="ESTACIONAMIENTO")
    etiquet.config(font=('Ravie',24))
    etiquet.pack()
    """
    foto = PhotoImage(file='Estacioamiento.png')
    imagen_etiqueta = Label(pantalla,image=foto)
    imagen_etiqueta.pack()"""
    
    reserva=Button(pantalla,text="Reserva",command=Reserva)
    reserva.pack(pady=5,padx=0)
    reserva.config(font=('Ravie',14))

    inicio=Button(pantalla,text="LOGIN ADMINISTRATIVO",command=login)
    inicio.pack(pady=10,padx=0)
    inicio.config(font=('Ravie',10))
    
    

    pantalla.mainloop()


   

def Reserva():
    global pantalla1
    pantalla1=Toplevel(pantalla)
    pantalla1.geometry("1080x540")
    pantalla1.title("RESERVA")
    pantalla1.iconbitmap("icono.ico")
    mi_frame=Frame(pantalla1)
    #imagenes
    """foto=PhotoImage(file='Estacioamiento.png')
    iM=Label(mi_frame,image=foto)
    iM.place(y=0,x=1)"""
    
    mi_frame.pack(expand=True,fill='both')
    mi_frame.config(bd=20)
    mi_frame.config(relief="solid")
    mi_frame.config(bg="#C8A2C8")
    #Etiquetas
    id_vehiculo=Label(mi_frame,text="ID VEHICULO")
    id_vehiculo.grid(row=0,column=0)
    id_vehiculo.config(font=('ravie',13))
    
    vehiculo=Label(mi_frame,text="seleccione vehiculo")
    vehiculo.grid(row=2,column=0)
    vehiculo.config(font=('ravie',12))

    ma=Label(mi_frame,text="MATRICULA DEL VEHICULO")
    ma.grid(row=6,column=0)
    
    ma.config(font=('ravie',12))

    MV=Label(mi_frame,text="MARCA")
    MV.grid(row=8,column=0)
    MV.config(font=('ravie',13))


    MOV=Label(mi_frame,text="MODELO DE VEHICULO")
    MOV.grid(row=10,column=0)
    MOV.config(font=('ravie',13))

    nom=Label(mi_frame,text="Nombre Dueño")
    nom.grid(row=12,column=0)
    nom.config(font=('ravie',13))

    dni=Label(mi_frame,text="DNI DE VEHICULO")
    dni.config(font=('ravie',13))
    dni.grid(row=14,column=0)

    hdi=Label(mi_frame,text="HORA DE INGRESO")
    hdi.config(font=('ravie',13))
    hdi.grid(row=16,column=0)



    #caja de texto
    idV=StringVar()
    
    Matic=StringVar()
    Mar=StringVar()
    Mod=StringVar()
    Nom=StringVar()
    Dni=StringVar()
    Hoi=StringVar()
    minu=StringVar()

    id_v=Entry(mi_frame,textvariable=idV,width=20)
    id_v.grid(row=0,column=2)

    opc=["AUTOMOVIL","MOTO"]
    OP=ttk.Combobox(mi_frame,width=20,values=opc,state="readonly")  
    OP.grid(row=2,column=2) 

    matic=Entry(mi_frame,textvariable=Matic,width=20)
    matic.grid(row=6,column=2)

    mar=Entry(mi_frame,textvariable=Mar,width=20)
    mar.grid(row=8,column=2)
    mod=Entry(mi_frame,textvariable=Mod,width=20)
    mod.grid(row=10,column=2)
    
    nomb=Entry(mi_frame,textvariable=Nom,width=20)
    nomb.grid(row=12,column=2)

    DNI=Entry(mi_frame,textvariable=Dni,width=20)
    DNI.grid(row=14,column=2)

    Hora = Spinbox(mi_frame,from_=0,to=23,textvariable=minu,width=5)
    Hora.grid(row=16,column=2)
    Hora.config(font=('Times',10,BOLD))  

    mi = Spinbox(mi_frame,from_=0,to=59,textvariable=Hoi,width=5)
    mi.grid(row=16,column=3)
    mi.config(font=('Times',10,BOLD))
    #botones
    re=Button(mi_frame,text="REGISTRAR ")
    re.grid(row=24,column=0)
    re.config(font=('Times',14,BOLD),bg='blue')
    



    EXIT=Button(mi_frame,text="VOLVER AL INICIO",command=pantalla1.destroy)
    EXIT.config(font=('Times',14,BOLD),bg='blue')
    EXIT.grid(row=24,column=2)

    

    


    
    mi_frame1=Frame(pantalla1)
    mi_frame1.pack(pady=15,padx=0)
    mi_frame1.config(bg="#7FFFD4")
    #Etiquetas
    
    #Botones

#HAGO ESTA FUNCION PARA PONER LOS MENSAJES    




conn=sqlite3.connect('login.db')
c=conn.cursor()

def create_table():
	c.execute("CREATE TABLE IF NOT EXISTS usuarios(Nombre TEXT,Apellido TEXT ,Usuario TEXT,Pass TEXT)")
	conn.commit()
	c.close()
	conn.close()

create_table()


										#Posicion de 'caja2'

def login():
    global Ventana
    ventana=Toplevel(pantalla)
    ventana.title("_Mi primer Login_")	#Titulo de la ventana principal
    ventana.geometry("280x450+300+250")	#Tamaño de nuestra ventana Principal
	
    color='#c5e2f6'			#Codigo HEX del color de fondo usado
    ventana['bg']=color		#Definimos nuestra ventana 'bg' con el valor 'color'

    Label(ventana,bg=color,text="Login",font=("Arial Black",16)).pack()	#Mostramos texto 'Login'

    #Abrir imagen para ventana principal
    imagen=Image.open("t.jpg")						#Abrimos la imagen 'logo.png'
    imagen=imagen.resize((180,180),Image.ANTIALIAS)		#Redimensionamos la imagen a 180x180
    photoImg=ImageTk.PhotoImage(imagen)					#Le damos nombre a nuestra imagen redimensionada (photoImg)
    panel=tk.Label(ventana,image=photoImg).pack()		#Mostramos la imagen en nuestra ventana
#Abrir imagen para ventana de registro
    img_reg=Image.open("th.jpg")						#Abrimos la imagen 'rak.jpg'
    img_reg=img_reg.resize((100,220),Image.ANTIALIAS)	#Redimensionamos la imagen
    photo_reg=ImageTk.PhotoImage(img_reg)				#Le damos nombre a nuestra imagen redimensionada (photo_reg)
#Cajas de nuestra ventana Principal
    Label(ventana,text="Usuario : ",bg=color,font=("Arial Black",10)).pack()	#Texto 'Usuario:'
    caja1=Entry(ventana,font=("Arial",10))										#Creamos una caja de texto 'caja1'
    caja1.pack()																#Posicion de la 'caja1'
    Label(ventana,text="Contraseña : ",bg=color,font=("Arial Black",10)).pack()	#Texto 'Contraseña:'
    caja2=Entry(ventana,show="*")												#Creamos la 'caja2' (contraseña)
    caja2.pack()																#Posicion de 'caja2'

    db=sqlite3.connect('login.db')		#Nos conectamos a nuestra base de datos 'login.db'
    c=db.cursor()						#Establecemos un cursor
	usuario=caja1.get()		#Obtenemos el valor de la 'caja1' (usuario)
	contr=caja2.get()		#Obtenemos el valor de la 'caja2' (contraseña)
	c.execute('SELECT * FROM usuarios WHERE Usuario = ? AND Pass = ?',(usuario,contr))	#Seleccionamos datos '(usuario,contr)'
	if c.fetchall():
		mb.showinfo(title="Login Correcto",message="Usuario y contraseña correctos")		#Mostramos 'Login Correcto'
	else:
		mb.showerror(title="Login incorrecto",message="Usuario o contraseña incorrecto")	#Mostramos 'Login incorrecto'
	#c.close()


def nuevaVentana():
    global newVentana							#Funcion nuevaVentana ... Nos permitira el registro de nuevos usuarios
	newVentana=tk.Toplevel(pantalla)			#Definimos 'newVentana'
	newVentana.title("Registro de Usuario")	#Le damos el titulo 'Registro de Usuario'
	newVentana.geometry("300x290+800+250")	#Tamaño de la ventana
	newVentana['bg']=color					#Definimos newVentana 'bg' con el valor de 'color'
	
	labelExample=tk.Label(newVentana,text="Registro : ",bg=color,font=("Arial Black",12)).pack(side="top")	#Texto 'Registro'
	panel_reg=tk.Label(newVentana,image=photo_reg).pack(side="left")	#Mostramos la imagen en la posicion 'left' (Izquierda)

	Label(newVentana,text="Nombre : ",bg=color,font=("Arial Black",10)).pack()		#Texto 'Nombre:'
	caja3=Entry(newVentana)															#Creamos 'caja3' (Nombre)
	caja3.pack()
	Label(newVentana,text="Apellidos : ",bg=color,font=("Arial Black",10)).pack()	#Texto 'Apellidos'
	caja4=Entry(newVentana)															#Creamos 'caja4' (Apellidos)
	caja4.pack()
	Label(newVentana,text="Usuario : ",bg=color,font=("Arial Black",10)).pack()		#Texto 'Usuario'
	caja5=Entry(newVentana)															#Creamos 'caja5' (Usuario)
	caja5.pack()
	Label(newVentana,text="Contraseña : ",bg=color,font=("Arial Black",10)).pack()	#Texto 'Contraseña'
	caja6=Entry(newVentana,show="*")												#Creamos 'caja6' (Contraseña)
	caja6.pack()	
	Label(newVentana,text="Repita la Contraseña : ",bg=color,font=("Arial Black",10)).pack()	#Texto 'Repita la Contraseña'
	caja7=Entry(newVentana,show="*")															#Creamos 'caja7' 
	caja7.pack()
	def registro():				#Funcion registro ... Nos permitira escribir los datos a nuestra base de datos
		Nombre=caja3.get()		#Obtenemos el valor de 'caja3'
		Apellido=caja4.get()	#Obtenemos el valor de 'caja4'
		Usr_reg=caja5.get()		#Obtenemos el valor de 'caja5'
		Contra_reg=caja6.get()	#Obtenemos el valor de 'caja6'
		Contra_reg_2=caja7.get() #Obtenemos el valor de 'caja7'
		if(Contra_reg==Contra_reg_2):		#Esta condicion nos permite saber si las contraseñas coinciden
			#El siguiente comando es el encargado de insertar los datos obtenidos en el registro
			c.execute("INSERT INTO usuarios values(\'"+Nombre+"\',\'"+Apellido+"\',\'"+Usr_reg+"\',\'"+Contra_reg+"')")
			db.commit()			#Confirmamos los datos
			mb.showinfo(title="Registro Correcto",message="Hola "+Nombre+" "+Apellido+" ¡¡ \nSu registro fue exitoso.")
			newVentana.destroy()		#Cerramos la ventana de registro
		else:	#Se ejecutara si las contraseñas no coinciden
			mb.showerror(title="Contraseña Incorrecta",message="Error¡¡¡ \nLas contraseñas no coinciden.")	#Mostramos un mensaje
		#c.close()		#Nos permite cerrar el cursor ...
		#db.close()
	#El siguiente comando (boton) nos permite llamar ala funcion registro
	buttons=tk.Button(newVentana,text="Registrar ¡",command=registro,bg=color,font=("Arial Rounded MT Bold",10)).pack(side="bottom")
	
Label(ventana,text=" ",bg=color,font=("Arial",10)).pack()		#Solo es una linea vacia ... (lo use para separar el boton) 
Button(text=" ENTRAR ",command=login,bg='#a6d4f2',font=("Arial Rounded MT Bold",10)).pack()		#Boton ==> funcion 'login'
Label(ventana,text=" ",bg=color,font=("Arial Black",10)).pack()
Label(ventana,text="No tienes una cuenta ? : ",bg=color,font=("Arial Black",10)).pack()		#Simple texto
#La siguiente linea (boton) nos llama ala funcion 'nuevaVentana' ==> ( ventana de registro)
boton1=Button(ventana,text="REGISTRO",bg='#a6d4f2',command=nuevaVentana,font=("Arial Rounded MT Bold",10)).pack()

ventana.mainloop()


 

"""def inicio_secion():
    global panatalla2
    pantalla2=Toplevel(pantalla)
    pantalla2.geometry("400x550")
    pantalla2.title("LOGIN")
    pantalla2.iconbitmap("icono.ico")
    pantalla2.config(bg="#C8A2C8")

    
    Usua=Label(pantalla2,text="usuario")
    Usua.config(font=('Ravie',18))
    Usua.pack() 
    usu=StringVar()
    usuario=Entry(pantalla2,textvariable=usu,width=20)
    usuario.pack(pady=2,padx=0)
    cont=Label(pantalla2,text="Contraseña")
    cont.config(font=('Ravie',18))
    cont.pack(pady=3,padx=0)
    contra=StringVar()
    contraseña=Entry(pantalla2,textvariable=contra,show="*")
    contraseña.pack(pady=4,padx=0)
    entra=Button(pantalla2,text="Entrar",command=correcta)
    entra.pack(pady=5,padx=3)
    #CONTRA Y USUARIO 
    name=usuario.get()
    password=contraseña.get()
    if name== "admin" and password == "estacionamiento":
        correcta()

def correcta():
    global panatalla3
    pantalla3=Toplevel(pantalla)
    pantalla3.geometry("400x550")
    pantalla3.title("LOGIN")
    pantalla3.iconbitmap("icono.ico")
    pantalla3.config(bg="#C8A2C8")


"""

Menu()
