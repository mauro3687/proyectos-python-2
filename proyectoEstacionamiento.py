from cProfile import label
from cgitb import text
from ctypes.wintypes import SIZE
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

conn=sqlite3.connect('login.db')
c=conn.cursor()

def menu():
    global ventana 
    ventana=Tk()
    ventana.title("BIENVENIDOS")
    ventana.geometry('1280x720+0+0')
    ventana.iconbitmap("icono.ico")
    
    
   
    
    

    menu=Menu(ventana)
    ventana.config(menu=menu)

    

    
    menu.add_cascade(label='administracion')
    menu.add_cascade(label='REGISTRO',command=Registro)
    menu.add_cascade(label='CARGA DE SALDO',command=carga)
    menu.add_cascade(label='ABONADOS',command=abonados)
    menu.add_cascade(label='SALIR',command=salir)
  
    ventana.mainloop()


def Registro ():
    global ventana1
    ventana1=Toplevel(ventana)
    ventana1.title("registro")
    ventana1.iconbitmap("icono.ico")
    mi_frame=Frame(ventana1)
    #imagenes
    foto=PhotoImage(file='Estacioamiento.png')
    iM=Label(mi_frame,image=foto)
    iM.place(y=0,x=1)
    
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
    



    EXIT=Button(mi_frame,text="VOLVER AL INICIO",command=ventana1.destroy)
    EXIT.config(font=('Times',14,BOLD),bg='blue')
    EXIT.grid(row=24,column=2)

    

    


    
    mi_frame1=Frame(ventana1)
    mi_frame1.pack(pady=15,padx=0)
    mi_frame1.config(bg="#7FFFD4")


def carga():
    global ventana2
    ventana2=Toplevel(ventana)
    ventana2.title("CARGA DE SALDO")
    ventana2.geometry("200x150")
    ventana2.iconbitmap("icono.ico")
    mi_frame=Frame(ventana2)
    mi_frame.pack(expand=True,fill='both')
    mi_frame.config(bd=20)
    mi_frame.config(relief="solid")
    mi_frame.config(bg="#C8A2C8")

    #ETIQUETA 
    DNI=Label(mi_frame,text="DNI").grid()
    
    carga=Label(mi_frame,text="carga").grid(row=1,column=0)

    #caja
    dni=StringVar() 
    cajaD=Entry(mi_frame,textvariable=dni,width=20).grid(row=0,column=1)

    patente=StringVar()
    cajas=Entry(mi_frame,textvariable=carga,width=20).grid(row=1,column=1)

    Button1=Button(mi_frame,text="cargar",command=mb).grid(row=4,column=0)
    Button2=Button(mi_frame,text="salir",command=ventana2.destroy).grid(row=4,column=1)

    cargas=cajas.get()
    dnis=cajaD.get()
     
    mb.showinfo(title="carga de saldo",message="SU SALDO ES:"+cargas+""+dnis+"\n fue realizada con exito" )
    






def abonados():
    global ventana3
    ventana3=Toplevel(ventana)
    ventana3.title("ABONADOS")
    ventana3.iconbitmap("icono.ico")
    ventana3.geometry("200x150")
    mi_frame=Frame(ventana3)
    mi_frame.pack(expand=True,fill='both')
    mi_frame.config(bd=20)
    mi_frame.config(relief="solid")
    mi_frame.config(bg="#c5e2f6")

    #ETIQUETA 
    DNI=Label(mi_frame,text="DNI").grid()
    pate=Label(mi_frame,text="PATENTE").grid(row=1,column=0)

    #cajs
    dni=StringVar()
    paten=StringVar()

    cajaD=Entry(mi_frame,textvariable=dni,width=20).grid(row=0,column=1)
    caja2=Entry(mi_frame,textvariable=paten,width=20).grid(row=1,column=1)
    #boton

    bot=Button(mi_frame,text="guardar").grid(row=2,column=0)
    

    bot1=Button(mi_frame,text="salir",command=ventana3.destroy).grid(row=2,column=1)

    

def salir():
    ventana.destroy

def create_table():
	c.execute("CREATE TABLE IF NOT EXISTS usuarios(Nombre TEXT,Apellido TEXT ,Usuario TEXT,Pass TEXT)")
	conn.commit()
	c.close()
	conn.close()

create_table()                            
ventana4=tk.Tk()
ventana4.title("inicio de sesion")
ventana4.iconbitmap("icono.ico")
ventana4.geometry("1280x720+0+0")	
	
color='#c5e2f6'			
ventana4['bg']=color		

Label(ventana4,bg=color,text="Login",font=("Arial Black",16)).pack()

#Abrir imagen para ventana principal
imagen=Image.open("t.jpg")						
imagen=imagen.resize((180,180),Image.ANTIALIAS)		
photoImg=ImageTk.PhotoImage(imagen)					
panel=tk.Label(ventana4,image=photoImg).pack()		
#Abrir imagen para ventana de registro
img_reg=Image.open("th.jpg")						
img_reg=img_reg.resize((100,220),Image.ANTIALIAS)
photo_reg=ImageTk.PhotoImage(img_reg)				
#Cajas de nuestra ventana Principal
Label(ventana4,text="Usuario : ",bg=color,font=("Arial Black",10)).pack()	
caja1=Entry(ventana4,font=("Arial",10))										
caja1.pack()																
Label(ventana4,text="Contraseña : ",bg=color,font=("Arial Black",10)).pack()	
caja2=Entry(ventana4,show="*")												
caja2.pack()																

db=sqlite3.connect('guarda_login.db')		
c=db.cursor()						

def login():
    				
	usuario=caja1.get()		
	contr=caja2.get()		
	c.execute('SELECT * FROM usuarios WHERE Usuario = ? AND Pass = ?',(usuario,contr))	
	if c.fetchall():
		menu()		
	else:
		mb.showerror(title="Login incorrecto",message="Usuario o contraseña incorrecto")	
	#c.close()



def nuevaVentana():							
	newVentana=tk.Toplevel(ventana4)			
	newVentana.title("Registro de Usuario")	
	newVentana.geometry("300x290+800+250")
    
	newVentana['bg']=color					
	
	labelExample=tk.Label(newVentana,text="Registro : ",bg=color,font=("Arial Black",12)).pack(side="top")	
	panel_reg=tk.Label(newVentana,image=photo_reg).pack(side="left")	#

	Label(newVentana,text="Nombre : ",bg=color,font=("Arial Black",10)).pack()	
	caja3=Entry(newVentana)															
	caja3.pack()
	Label(newVentana,text="Apellidos : ",bg=color,font=("Arial Black",10)).pack()	
	caja4=Entry(newVentana)															
	caja4.pack()
	Label(newVentana,text="Usuario : ",bg=color,font=("Arial Black",10)).pack()		
	caja5=Entry(newVentana)															
	caja5.pack()
	Label(newVentana,text="Contraseña : ",bg=color,font=("Arial Black",10)).pack()	
	caja6=Entry(newVentana,show="*")												
	caja6.pack()	
	Label(newVentana,text="Repita la Contraseña : ",bg=color,font=("Arial Black",10)).pack()	
	caja7=Entry(newVentana,show="*")															
	caja7.pack()
	def registro():				
		Nombre=caja3.get()		
		Apellido=caja4.get()	
		Usr_reg=caja5.get()		
		Contra_reg=caja6.get()	
		Contra_reg_2=caja7.get() 
		if(Contra_reg==Contra_reg_2):		
			
			c.execute("INSERT INTO usuarios values(\'"+Nombre+"\',\'"+Apellido+"\',\'"+Usr_reg+"\',\'"+Contra_reg+"')")
			db.commit()			
			mb.showinfo(title="Registro Correcto",message="Hola "+Nombre+" "+Apellido+" ¡¡ \nSu registro fue exitoso.")
			newVentana.destroy()		
		else:	
			mb.showerror(title="Contraseña Incorrecta",message="Error¡¡¡ \nLas contraseñas no coinciden.")	#Mostramos un mensaje
		#c.close()		
		#db.close()
	
	buttons=tk.Button(newVentana,text="Registrar ",command=registro,bg=color,font=("Arial Rounded MT Bold",10)).pack(side="bottom")
	
Label(ventana4,text=" ",bg=color,font=("Arial",10)).pack()		
Button(text=" ENTRAR ",command=login,bg='#a6d4f2',font=("Arial Rounded MT Bold",10)).pack()		
Label(ventana4,text=" ",bg=color,font=("Arial Black",10)).pack()
Label(ventana4,text="No tienes una cuenta ? : ",bg=color,font=("Arial Black",10)).pack()		

boton1=Button(ventana4,text="REGISTRO",bg='#a6d4f2',command=nuevaVentana,font=("Arial Rounded MT Bold",10)).pack()


ventana4.mainloop()