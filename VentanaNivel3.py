import tkinter as tk
import sqlite3
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
from tkinter import *

class Nivel3(Frame):
    '''
    Función: Abrir 
    Propósito: Abre la base de datos SQLITE
    '''
    def abrir(self):
        conexion=sqlite3.connect('BDProyectoGr1.db')
        return conexion
    '''
    Función: __init__
    Propósito: Crear el notebook donde se van a montar las pestañas de las busquedas 
    '''
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        master.title("USUARIO NIVEL 3")
        
        self.cuaderno1 = ttk.Notebook(master)       
        self.consultaProductos()
        self.consultaClientes()
        self.consultaProveedores()
        self.cuaderno1.grid(column=0, row=0, padx=50, pady=50)
    '''
    Función: consultaProductos
    Propósito: Crear la pestaña donde se va a realizar la busqueda de los productos
    Variables involucradas: codigo, nombre y costo del producto
    '''
    def consultaProductos(self):
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Consulta de productos")
        
        self.labelframe1=ttk.LabelFrame(self.pagina1, text="Ingrese codigo de producto")        
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        
        self.label1=ttk.Label(self.labelframe1, text="Codigo:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.codprod=tk.StringVar()
        self.entrycodprod=ttk.Entry(self.labelframe1, textvariable=self.codprod)
        self.entrycodprod.grid(column=1, row=0, padx=4, pady=4)
        
        self.label2=ttk.Label(self.labelframe1, text="Nombre:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.nomprod=tk.StringVar()
        self.entrynomprod=ttk.Entry(self.labelframe1, textvariable=self.nomprod,state="readonly")
        self.entrynomprod.grid(column=1, row=1, padx=4, pady=4)
        
        self.label3=ttk.Label(self.labelframe1, text="Costo:")        
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.costoprod=tk.StringVar()
        self.entrycostoprod=ttk.Entry(self.labelframe1, textvariable=self.costoprod, state="readonly")
        self.entrycostoprod.grid(column=1, row=2, padx=4, pady=4)
        
        self.boton1=ttk.Button(self.labelframe1, text="Buscar", command=self.buscarProductos)
        self.boton1.grid(column=1, row=4, padx=4, pady=4)
    '''
    Función: consultaClientes
    Propósito: Crear la pestaña donde se va a realizar la busqueda de los clientes
    Variables involucradas: codigo, nombre, direccion, telefono y ciudad del cliente
    '''
    def consultaClientes(self):
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Consulta de clientes")
        
        self.labelframe2=ttk.LabelFrame(self.pagina2, text="Ingrese codigo de cliente")        
        self.labelframe2.grid(column=0, row=0, padx=5, pady=10)
        
        self.label1=ttk.Label(self.labelframe2, text="Codigo:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.codclie=tk.StringVar()
        self.entrycodclie=ttk.Entry(self.labelframe2, textvariable=self.codclie)
        self.entrycodclie.grid(column=1, row=0, padx=4, pady=4)
        
        self.label2=ttk.Label(self.labelframe2, text="Nombre:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.nomclie=tk.StringVar()
        self.entrynomclie=ttk.Entry(self.labelframe2, textvariable=self.nomclie,state="readonly")
        self.entrynomclie.grid(column=1, row=1, padx=4, pady=4)
        
        self.label3=ttk.Label(self.labelframe2, text="Direccion:")        
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.direc=tk.StringVar()
        self.entrydirec=ttk.Entry(self.labelframe2, textvariable=self.direc, state="readonly")
        self.entrydirec.grid(column=1, row=2, padx=4, pady=4)

        self.label4=ttk.Label(self.labelframe2, text="Telefono:")        
        self.label4.grid(column=0, row=3, padx=4, pady=4)
        self.telef=tk.StringVar()
        self.entrytelef=ttk.Entry(self.labelframe2, textvariable=self.telef, state="readonly")
        self.entrytelef.grid(column=1, row=3, padx=4, pady=4)
        
        self.label5=ttk.Label(self.labelframe2, text="Ciudad:")        
        self.label5.grid(column=0, row=4, padx=4, pady=4)
        self.ciudad=tk.StringVar()
        self.entryciudad=ttk.Entry(self.labelframe2, textvariable=self.ciudad, state="readonly")
        self.entryciudad.grid(column=1, row=4, padx=4, pady=4)

        self.boton1=ttk.Button(self.labelframe2, text="Buscar", command=self.buscarClientes)
        self.boton1.grid(column=1, row=5, padx=4, pady=4)
    '''
    Función: consultaProveedores
    Propósito: Crear la pestaña donde se va a realizar la busqueda de los proveedores
    Variables involucradas: id del proveedor, codigo y costo del producto
    '''
    def consultaProveedores(self):
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Consulta de proveedores")
        
        self.labelframe2=ttk.LabelFrame(self.pagina2, text="Ingrese ID de proveedor")        
        self.labelframe2.grid(column=0, row=0, padx=5, pady=10)
        
        self.label1=ttk.Label(self.labelframe2, text="ID:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.idprov=tk.StringVar()
        self.entryidprov=ttk.Entry(self.labelframe2, textvariable=self.idprov)
        self.entryidprov.grid(column=1, row=0, padx=4, pady=4)
        
        self.label2=ttk.Label(self.labelframe2, text="Codigo productos:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.codprodaux=tk.StringVar()
        self.entrycodprodaux=ttk.Entry(self.labelframe2, textvariable=self.codprodaux,state="readonly")
        self.entrycodprodaux.grid(column=1, row=1, padx=4, pady=4)
        
        self.label3=ttk.Label(self.labelframe2, text="Costos:")        
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.costoprov=tk.StringVar()
        self.entrycostoprov=ttk.Entry(self.labelframe2,textvariable=self.costoprov, state="readonly")
        self.entrycostoprov.grid(column=1, row=2, padx=4, pady=4)

        self.boton1=ttk.Button(self.labelframe2, text="Buscar", command=self.buscarProveedores)
        self.boton1.grid(column=1, row=3, padx=4, pady=4)
    '''
    Función: buscarProductos
    Propósito: Crear una tupla que sera la encargada de comparar con la informacion de la base de datos
    Variables involucradas: codigo, nombre y costo del producto
    '''
    def buscarProductos(self):
        datos=(self.codprod.get(), )
        respuesta=self.consultaP(datos)
        if len(respuesta)>0:
            self.nomprod.set(respuesta[0][0])
            self.costoprod.set(respuesta[0][1])
        else:
            self.nomprod.set('')
            self.costoprod.set('')
            mb.showinfo("Información", "No existe un producto con dicho código")
    '''
    Función: consultaP
    Propósito: Abrir la base de datos y dirigirse a la tabla del producto para comparar su codigo
    Variables involucradas: codigo, nombre y costo del producto
    '''
    def consultaP(self, datos):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select nomprod, costoprod from productos where codprod=?"
            cursor.execute(sql, datos)
            return cursor.fetchall()
        finally:
            cone.close()            
    '''
    Función: buscarClientes
    Propósito:Crear una tupla que sera la encargada de comparar con la informacion de la base de datos
    Variables involucradas: codigo, nombre y direccion, telefono y ciudad del cliente
    '''
    def buscarClientes(self):
        datos=(self.codclie.get(), )
        respuesta=self.consultaC(datos)
        if len(respuesta)>0:
            self.nomclie.set(respuesta[0][0])
            self.direc.set(respuesta[0][1])
            self.telef.set(respuesta[0][2])
            self.ciudad.set(respuesta[0][3])
        else:
            self.nomclie.set('')
            self.direc.set('')
            self.telef.set('')
            self.ciudad.set('')
            mb.showinfo("Información", "No existe un cliente con dicho código")
    '''
    Función: consultaC
    Propósito: Abrir la base de datos y dirigirse a la tabla de cliente para comparar el codigo
    Variables involucradas: codigo, nombre y direccion, telefono y ciudad del cliente
    '''           
    def consultaC(self, datos):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select nomclie, direc, telef, ciudad from clientes where codclie=?"
            cursor.execute(sql, datos)
            return cursor.fetchall()
        finally:
            cone.close()
    '''
    Función: buscarProveedores
    Propósito:Crear una tupla que sera la encargada de comparar con la informacion de la base de datos
    Variables involucradas: id del proveedor, codigo y costo del producto
    '''
    def buscarProveedores(self):
        datos=(self.idprov.get(), )
        respuesta=self.consultaPr(datos)
        if len(respuesta)>0:
            self.codprodaux.set(respuesta[0][0])
            self.costoprov.set(respuesta[0][1])
        else:
            self.codprodaux.set('')
            self.costoprov.set('')
            mb.showinfo("Información", "No existe un proveedor con dicho código")
    '''
    Función: consultaC
    Propósito: Abrir la base de datos y dirigirse a la tabla de proveedor, buscar el id
    Variables involucradas: id del proveedor, codigo y costo del producto
    '''            
    def consultaPr(self, datos):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select codprodaux, costoprov from proveedores where idprov=?"
            cursor.execute(sql, datos)
            return cursor.fetchall()
        finally:
            cone.close()
            

