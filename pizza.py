from tkinter import*
from tkinter import ttk
from tkinter import messagebox

def menu():
    global raiz
    raiz=Tk()
    raiz.geometry("1280x720")
    raiz.config(bg="#C8A2C8")
    raiz.iconbitmap("icono_pizza.ico")

    menu=Menu(raiz)
    raiz.config(menu=menu)

    

    
    menu.add_cascade(label='toma de pedido',command=toma)
    menu.add_cascade(label='stock de ingrediento',command=stock)
    menu.add_cascade(label='administracion',command=admin)
    menu.add_cascade(label='cantidad de ventas',command=cantidad)
    menu.add_cascade(label='SALIR',command=salir)
  
    raiz.mainloop()


def toma():
    global raiz1
    raiz1=Toplevel(raiz)
    raiz1.geometry("800x450")
    raiz1.config(bg="Darkorange2")
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

    etiBa=Label(raiz1,text="BARRIO").pack(ipady=1,ipadx=1)
    etiCa=Label(raiz1,text="CALLE")
    etiN=Label(raiz1,text="NUMERO")
    etiD=Label(raiz1,text="DEPARTAMENTO")
    
    

    

    
    
    
    


def stock():
    global raiz2
    raiz2=Toplevel(raiz)
    raiz2.geometry("300x150")
    raiz2.config(bg="#F0F8FF")
    raiz2.iconbitmap("icono_pizza.ico")

    s=Label(raiz2,text="STOCK")
    s.config(font=('Times',22),bg='#00FFFF')
    s.pack()

    

def admin():
    global raiz3
    raiz3=Toplevel(raiz)
    raiz3.geometry("300X150")
    raiz3.config(bg="#F0F8FF")
    raiz3.iconbitmap("icono_pizza.ico")

    
    

def cantidad():
    global raiz4
    raiz4=Toplevel(raiz)
    raiz4.geometry("300x150")
    raiz4.config(bg="#F0F8FF")
    raiz4.iconbitmap("icono_pizza.ico")
    
def salir():
    global raiz
    Salir=messagebox.askokcancel("Atencion","¿Desea salir de la aplicacion?")
       
    if Salir==True:
        raiz.destroy()
menu()


    
