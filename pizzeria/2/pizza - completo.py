from ctypes import resize
from email.mime import image
from tkinter import*
from tkinter import ttk
from tkinter import messagebox

def menu():
    global raiz
    raiz=Tk()
    raiz.attributes('-fullscreen',True)
    raiz.title("PIZZERIA")
    raiz.config(bg="#C8A2C8")
    raiz.iconbitmap("icono_pizza.ico")

    menu=Menu(raiz)
    
    
    raiz.config(menu=menu)

    

    
    menu.add_cascade(label='toma de pedido',command=toma)
    menu.add_cascade(label='pedido presencial',command=toma2)
    menu.add_cascade(label='administracion',command=admin)
    
    menu.add_cascade(label='SALIR',command=salir)

    mi_frame1=Frame(raiz)

    
    mi_frame1.config(bd=5)
    mi_frame1.config(width="400",height="720")
    mi_frame1.config(relief="solid")
    mi_frame1.config(bg="Darkgoldenrod1")
    mi_frame1.place(x=-1,y=0)

    boto1=Button(mi_frame1,text="control\n de \n pedido",command=cantidad)
    boto1.config(font=('Times',45),bg='Dark orange4')
    boto1.place(x=-1,y=0,width=400,height=240)
    boto2=Button(mi_frame1,text="ingreso \n de \n producto",command=ingreso)
    boto2.config(font=('Times',45),bg='Dark green')
    boto2.place(x=-1,y=240,width=400,height=240)
    boton3=Button(mi_frame1,text="presente el \n vendedor",command=login)
    boton3.config(font=('Times',35),bg='Dark orange')
    boton3.place(x=-1,y=480,width=400,height=240)


    foto=PhotoImage(file="logo3.png")
    
    image=Label(raiz,image=foto).place(x=680,y=250)
    
#expand=True,padx=0,pady=20
  
    raiz.mainloop()
    
    



def toma():
    global raiz1
    raiz1=Toplevel(raiz)
    raiz1.geometry("1280x720")
    raiz1.config(bg="Darkorange2")
    raiz1.title("toma de pedido a domicilio")
    raiz1.iconbitmap("icono_pizza.ico")

   

    eti=Label(raiz1,text="DISEÑE SU PIZZA !!")
    eti.config(font=('Times',35),bg='#00FFFF')
    eti.pack()
    
    
    
    etiT=Label(raiz1,text="SELECCIONE EL TAMAÑO").pack(padx=0,pady=10)

    opc=["CHICA","FAMILIAR","PORCION"]
    OP=ttk.Combobox(raiz1,width=20,values=opc,state="readonly").pack(padx=0,pady=9)
    
    etiI=Label(raiz1,text="SELECCIONE INGREDIENTES").pack(padx=0,pady=8)
    
    opc1=["MUZZARELLA","NAPO","CALABRESA","ESPECIAL","CON HUEVO","FUGACETTA"]
    OP1=ttk.Combobox(raiz1,width=20,values=opc1,state="readonly").pack(padx=0,pady=7)

    etiP=Label(raiz1,text="SELECCIONE FORMA DE PAGO").pack(padx=0,pady=6)

    opc2=["TARJETA DE CREDITO","TARJETA DE DEBITO","TRANSFERENCIA","EFECTIVO"]
    
    OP2=ttk.Combobox(raiz1,width=20,values=opc2,state="readonly").pack(padx=0,pady=5)

    BU=Button(raiz1,text="HACER EL PEDIDO").pack(padx=1,pady=4)
   

    mi_frame=Frame(raiz1)
    mi_frame.pack(expand=True,fill='both',padx=0,pady=20)
    mi_frame.config(bd=5)
    mi_frame.config()
    mi_frame.config(relief="solid")
    mi_frame.config(bg="Darkgoldenrod1")
    #barrios
    etiBa=Label(mi_frame,text="BARRIO").grid(row=0,column=0)
    etiCa=Label(mi_frame,text="CALLE").grid(row=2,column=0)
    cajB=StringVar()
    cajc=StringVar()
    
    cajab=Entry(mi_frame,textvariable=cajB,width=20).grid(row=0,column=10,padx=2,pady=10)
    cajac=Entry(mi_frame,textvariable=cajc,width=20).grid(row=2,column=10,padx=0,pady=9)

    #
    cajN=StringVar()
    cajD=StringVar()
    
    cajan=Entry(mi_frame,textvariable=cajN,width=20).grid(row=0,column=200,padx=0,pady=10)
    cajad=Entry(mi_frame,textvariable=cajD,width=20).grid(row=2,column=200,padx=0,pady=9)

    


    etiN=Label(mi_frame,text="NUMERO").grid(row=0,column=100,pady=10,padx=2)
    etiD=Label(mi_frame,text="DEPARTAMENTO").grid(row=2,column=100,pady=9,padx=10)

    #
    etidaTOS=Label(mi_frame,text="DATOS DEL CLIENTE")
    etidaTOS.config(font=('Times',15),bg='#00FFFF')
    etidaTOS.grid(row=4,column=10,padx=0,pady=8)


    etiNOM=Label(mi_frame,text="NOMBRE").grid(row=5,column=0,padx=2,pady=10)
    etTEL=Label(mi_frame,text="TELEFONO").grid(row=7,column=0,padx=2,pady=10)
    #caja
    a=StringVar()
    b=StringVar()

    nomcaja=Entry(mi_frame,textvariable=a,width=20).grid(row=5,column=10,padx=2,pady=10)
    numcaja=Entry(mi_frame,textvariable=b,width=20).grid(row=7,column=10,padx=2,pady=10)
    #imagen
    imagen=PhotoImage(file='logo4.png')
    image_frame=Label(mi_frame,image=imagen).place(x=800,y=50)


    boton= Button (mi_frame,text="GUARDAR",width=10,height=5)
    
    boton.grid(row=5,column=20,padx=4,pady=20)

    #image2
    imagen1=PhotoImage(file='menu.png')
    image_menu=Label(raiz1,image=imagen1,height=325,width=280).place(x=0,y=0)
    
    #boton
    


    
    
    
    


def toma2():
    global raiz2
    raiz2=Toplevel(raiz)
    raiz2.geometry("1280x720")
    raiz2.config(bg="Darkorange2")
    raiz2.title("toma de pedido presencial")
    raiz2.iconbitmap("icono_pizza.ico")

    s=Label(raiz2,text="SELECCIONE TU PIZZA")
    s.config(font=('Times',22),bg='#00FFFF')
    s.pack() 
    etiT=Label(raiz2,text="SELECCIONE EL TAMAÑO").pack(padx=0,pady=10)

    opc=["CHICA","FAMILIAR","PORCION"]
    OP=ttk.Combobox(raiz2,width=20,values=opc,state="readonly").pack(padx=0,pady=9)
    
    etiI=Label(raiz2,text="SELECCIONE INGREDIENTES").pack(padx=0,pady=8)
    
    opc1=["MUZZARELLA","NAPO","CALABRESA","ESPECIAL","CON HUEVO","FUGACETTA"]
    OP1=ttk.Combobox(raiz2,width=20,values=opc1,state="readonly").pack(padx=0,pady=7)

    etiP=Label(raiz2,text="SELECCIONE FORMA DE PAGO").pack(padx=0,pady=6)

    opc2=["TARJETA DE CREDITO","TARJETA DE DEBITO","TRANSFERENCIA","EFECTIVO"]
    
    OP2=ttk.Combobox(raiz2,width=20,values=opc2,state="readonly").pack(padx=0,pady=5)

    BU=Button(raiz2,text="HACER EL PEDIDO").pack(padx=1,pady=4)
    

    mi_frame=Frame(raiz2)
    mi_frame.pack(expand=True,fill='both',padx=0,pady=20)
    mi_frame.config(bd=5)
    mi_frame.config()
    mi_frame.config(relief="solid")
    mi_frame.config(bg="Darkgoldenrod1")
    #barrios
    etiBa=Label(mi_frame,text="nombre del cliente").grid(row=0,column=0)
    etiCa=Label(mi_frame,text="numero de mesa").grid(row=2,column=0)
    cajB=StringVar()
    cajc=StringVar()
    
    cajab=Entry(mi_frame,textvariable=cajB,width=20).grid(row=0,column=10,padx=2,pady=10)
    cajac=Entry(mi_frame,textvariable=cajc,width=20).grid(row=2,column=10,padx=0,pady=9)

    #
    cajN=StringVar()
    cajD=StringVar()
    
    
   

    etiM=Label(mi_frame,text="EL TIPO DE PIZZA A ENTREGAR")
    etiM.config(font=('ravie',15))
    etiM.grid(row=5,column=0)


    opc2=["MUZZARELLA","NAPO","CALABRESA","ESPECIAL","CON HUEVO","FUGACETTA"]
    OP1=ttk.Combobox(mi_frame,width=20,values=opc2,state="readonly").grid(row=6,column=0,padx=0,pady=9)

    imagen=PhotoImage(file='logo4.png')
    image_frame=Label(mi_frame,image=imagen).place(x=800,y=50)


    boton= Button (mi_frame,text="GUARDAR",width=10,height=5)
    
    boton.grid(row=5,column=20,padx=8,pady=20)

    
    imagen1=PhotoImage(file='menu.png')
    image_menu=Label(raiz2,image=imagen1,height=310,width=280).place(x=0,y=0)
    
    

def admin():
    global raiz3
    raiz3=Toplevel(raiz)
    raiz3.geometry("600x400")
    raiz3.config(bg="#FF8000")
    raiz3.title("administracion")
    raiz3.iconbitmap("icono_pizza.ico")

    #cajs
    caja1=StringVar()
    caja2=StringVar()
    caja3=StringVar()
    caja4=StringVar()
    etic=Label(raiz3,text="cantidad de pizza vendidas").place(x=0,y=190)
    c=Entry(raiz3,textvariable=caja1,width=5).place(x=150,y=190)

    etip=Label(raiz3,text="pizza mas vendida").place(x=0,y=220)
    c1=Entry(raiz3,textvariable=caja2,width=5).place(x=150,y=220)

    etiv=Label(raiz3,text="vendedor con mas ventas").place(x=0,y=250)
    c2=Entry(raiz3,textvariable=caja3,width=5).place(x=150,y=250)

    etir=Label(raiz3,text="recaudacion del mes  ").place(x=0,y=280)
    c3=Entry(raiz3,textvariable=caja4,width=5).place(x=150,y=280)


    



    
    

def cantidad():
    global raiz4
    raiz4=Toplevel(raiz)
    raiz4.geometry("800x300")
    raiz4.config(bg="#FF8000")
    raiz4.title("ingreso de pedido")
    raiz4.iconbitmap("icono_pizza.ico")

    caja1=StringVar()
    caja2=StringVar()
    caja3=StringVar()
    caja4=StringVar()

    et=Label(raiz4,text="la pizza a entregar").place(x=0,y=0)
    caT=Entry(raiz4,textvariable=caja1,width=6).place(x=110,y=0)
    etn=Label(raiz4,text="numero de orden").place(x=0,y=30)
    can=Entry(raiz4,textvariable=caja1,width=6).place(x=110,y=30)
    etm=Label(raiz4,text="numero de mesa").place(x=0,y=60)
    cam=Entry(raiz4,textvariable=caja1,width=6).place(x=110,y=60)
    etd=Label(raiz4,text="numero de deliveri").place(x=0,y=90)
    cad=Entry(raiz4,textvariable=caja1,width=6).place(x=110,y=90)


    #foto
    imagen=PhotoImage(file='logo3.png')
    image_frame=Label(raiz4,image=imagen).place(x=400,y=50)



def ingreso():
    global raiz5
    raiz5=Toplevel(raiz)
    raiz5.geometry("800x300")
    raiz5.config(bg="#FF8000")
    raiz5.title("ingreso de producto")
    raiz5.iconbitmap("icono_pizza.ico")

    caja1=StringVar()
    caja2=StringVar()
    caja3=StringVar()
    caja4=StringVar()

    et=Label(raiz5,text="CANTIDAD DE PIZZA").place(x=0,y=0)
    caT=Entry(raiz5,textvariable=caja1,width=6).place(x=110,y=0)
    etn=Label(raiz5,text="CANTIDAD DE QUESO").place(x=0,y=30)
    can=Entry(raiz5,textvariable=caja1,width=6).place(x=110,y=30)
    etm=Label(raiz5,text="CANTIDAD DE SALSA").place(x=0,y=60)
    cam=Entry(raiz5,textvariable=caja1,width=6).place(x=110,y=60)
    etd=Label(raiz5,text="OTROS").place(x=0,y=90)
    cad=Entry(raiz5,textvariable=caja1,width=6).place(x=110,y=90)

    

    #foto
    imagen=PhotoImage(file='logo3.png')
    image_frame=Label(raiz5,image=imagen).place(x=400,y=50)



def login():
    global raiz6
    raiz6=Toplevel(raiz)
    raiz6.geometry("600x400")
    raiz6.config(bg="#FF8000")
    raiz6.title("login del empleado")
    raiz6.iconbitmap("icono_pizza.ico")
    caja1=StringVar()
    caja2=StringVar()
   

    imagen=PhotoImage(file='logo3.png')
    image_frame=Label(raiz6,image=imagen).place(x=150,y=0)


    ENO=Label(raiz6,text="nombre del empleado").place(x=180,y=200)
    caj=Entry(raiz6,textvariable=caja1,width=20).place(x=180,y=230)

    Eco=Label(raiz6,text="contraseña").place(x=180,y=260)
    caj2=Entry(raiz6,textvariable=caja2,width=20).place(x=180,y=290)

    boto=Button(raiz6,text="INGRESAR").place(x=160,y=320)

    boto1=Button(raiz6,text="REGISTAR",command=registro).place(x=240,y=320)



def registro():
    global raiz7
    raiz7=Toplevel(raiz)
    raiz7.geometry("600x400")
    raiz7.config(bg="#FF8000")
    raiz7.title("REGISTRO DE EMPLEADO")
    raiz7.iconbitmap("icono_pizza.ico")
    caja1=StringVar()
    caja2=StringVar()
   

    imagen=PhotoImage(file='logo3.png')
    image_frame=Label(raiz7,image=imagen).place(x=150,y=0)


    ENO=Label(raiz7,text="nombre del empleado").place(x=180,y=200)
    caj=Entry(raiz7,textvariable=caja1,width=20).place(x=180,y=230)

    Eco=Label(raiz7,text="contraseña").place(x=180,y=260)
    caj2=Entry(raiz7,textvariable=caja2,width=20).place(x=180,y=290)

    boto=Button(raiz7,text="REGISTAR").place(x=160,y=320)

   



def salir():
    global raiz
    Salir=messagebox.askokcancel("Atencion","¿Desea salir de la aplicacion?")
       
    if Salir==True:
        raiz.destroy()

menu()


    
