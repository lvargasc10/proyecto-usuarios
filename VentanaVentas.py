import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox as mb
import sqlite3
from hashlib import sha1

'''
Función: Clase principal de los usuarios
Propósito: Almacena las diferentes funciones de los usuarios y sus niveles.
'''
class Ventas(Frame):    
    '''
    Función: __init__ 
    Propósito: permite que la clase almacene los datos de la GUI  
    '''
    def __init__(self, master= None):
        super().__init__(master)
        self.master = master
        master.title("Ventas")           
        
        #Mensaje 
        self.mensaje = Label(master,text="", fg="RED")
        self.mensaje.grid(row=3, column=0, columnspan = 2 , sticky = W+E)

        # Tabla
        self.tree = ttk.Treeview(master,height=10, columns = 4)
        self.tree.grid(row= 5,column=0 , columnspan = 2)
        self.tree["columns"]=("#1","#2","#3","#4","#5","#6","#7")        
        
        self.tree.heading("#0", text = "Fecha",anchor = CENTER)
        self.tree.heading("#1", text = "Codigo Cliente",anchor = CENTER)
        self.tree.heading("#2", text = "Codigo Producto",anchor = CENTER)
        self.tree.heading("#3", text = "Nombre Producto",anchor = CENTER)
        self.tree.heading("#4", text = "Costo",anchor = CENTER)
        self.tree.heading("#5", text = "Cantidad",anchor = CENTER)
        self.tree.heading("#6", text = "Valor Iva",anchor = CENTER)
        self.tree.heading("#7", text = "Valor Total",anchor = CENTER)
        self.get_ventas()
        
    '''
    Función: run_query 
    Propósito: Realiza la conexión a la Base de Datos y ejecuta la consulta con los parametros correspondientes.  
    '''
    def run_query(self,query,parameters = ()):
        with sqlite3.connect("BDProyectoGr1.db") as conn:
            cursor = conn.cursor()
            result = cursor.execute(query,parameters)
            conn.commit()
        return result  

    '''
    Función: get_Ventas 
    Propósito: Limpia la tabla y obtiene la lista de usuarios de la BD.  
    ''' 
    def get_ventas(self):
        #Limpia la tabla
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        #Consultar los datos  
        query="SELECT*FROM Ventas ORDER BY codclie ASC"
        db_rows = self.run_query(query)
        for row in db_rows:
            self.tree.insert("",0,text= row[0], values = (row[1],row[2],row[3],row[4],row[5],row[6],row[7])) 
