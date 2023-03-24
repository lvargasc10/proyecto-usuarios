import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox as mb
import sqlite3

class Nivel2(Frame):
    
    '''
    Función: __init__ 
    Propósito: permite que la clase almacene los datos de la GUI  
    '''
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        master.title("USUARIO NIVEL 2")        
       
        self.frame = LabelFrame(master, text ="Registrar un nuevo producto")
        self.frame.grid(row = 0, column =0, columnspan = 3, pady = 20 )        
        
        self.lblcodigo = Label(self.frame,text ="Código").grid(row = 1 , column =0) # texto a mostrar
        self.codigo = Entry(self.frame) 
        self.codigo.grid(row=1, column =1) 

        #Nombre input
        self.lblnombre = Label(self.frame,text ="Nombre").grid(row = 2 , column =0)
        self.nombre = Entry(self.frame) 
        self.nombre.grid(row=2, column =1)     
               
        self.lblprice = Label(self.frame,text ="Precio").grid(row = 3 , column =0) 
        self.price = Entry(self.frame) 
        self.price.grid(row=3, column= 1) 
        # Boton añadir producto
        # en la fila 3 , donde columspan es espacio de 2 , y  sticky W+E ocupe todo el espacio de Este a oeste

        self.btnguardar =ttk.Button(self.frame, text = "Guardar Producto",command =self.add_producto ).grid(row=4,columnspan =2,sticky=W+E)
        self.btnborrar = ttk.Button(master,text = "Borrar", command=self.borrar_producto).grid(row = 5 , column = 0, sticky = W+E)
        self.btneditar = ttk.Button(master,text = "Editar", command=self.editar_producto).grid(row = 5 , column = 1, sticky = W+E)
        
        #Mensaje 
        self.mensaje = Label(master,text="", fg="RED")
        self.mensaje.grid(row=3, column=0, columnspan = 2 , sticky = W+E)

        # Tabla
        self.tree = ttk.Treeview(master,height=10, columns = 3)
        self.tree.grid(row= 4,column=0 , columnspan = 2)
        self.tree["columns"]=("one","two")
                
        self.tree.heading("#0", text = "Código",anchor = CENTER)
        self.tree.heading("#1", text = "Nombre",anchor = CENTER)
        self.tree.heading("#2", text = "precio",anchor = CENTER)
        self.get_productos()
        
    '''
    Función: run_query 
    Propósito: Realiza la conexión a la BB y ejecuta la consulta con los parametros correspondientes.  
    '''
    def run_query(self,query,parameters = ()):
        with sqlite3.connect("BDProyectoGr1.db") as conn:
            cursor = conn.cursor()
            result = cursor.execute(query,parameters)
            conn.commit()
        return result

    '''
    Función: get_productos 
    Propósito: Limpia la tabla y obtiene la lista de productos de la BD.  
    ''' 
    def get_productos(self):
        #Limpia la tabla
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        #Consultar los datos  
        query="SELECT*FROM productos ORDER BY codprod DESC"
        db_rows = self.run_query(query)
        for row in db_rows:
            self.tree.insert("",0,text= row[0], values = (row[1],row[2]))
            
    '''
    Función: validacion
    Propósito: valida que los campos del producto no estén vacios.
    '''         
    def validacion(self):
        return len(self.codigo.get())!=0 and len(self.nombre.get())!= 0 and len(self.price.get()) !=0
    
    '''
    Función: add_producto
    Propósito: Ejecuta la consulta para ingresar un producto a la BD
    '''
    def add_producto(self):
        try:
            if self.validacion():
                query = 'INSERT INTO productos VALUES(?, ?, ?)'
                parameters =  (self.codigo.get(),self.nombre.get(), self.price.get())
                self.run_query(query, parameters)
                mb.showinfo("Información", "Los datos fueron cargados")
                self.mensaje['text'] = 'Producto {} ha sido agregado satisfactoriamente'.format(self.nombre.get())
                self.codigo.delete(0, END)
                self.nombre.delete(0, END)
                self.price.delete(0, END)
            else:
                mb.showinfo("Informacion","Nombre y precio son requeridos")
            self.get_productos()
        except sqlite3.IntegrityError as e:
            mb.showinfo("Información", "El código ya esta registrado")
        self.codigo.delete(0, END)
        self.nombre.delete(0, END)
        self.price.delete(0, END)
        self.get_productos()
        
    '''
    Función: borrar_producto
    Propósito: ejecuta la consulta para eliminar un producto de la BD
    '''  
    def borrar_producto(self):
        try:
            self.tree.item(self.tree.selection())["values"][0]
        except IndexError as e:
            mb.showinfo("Error", "Por favor selecciona un registro")
            return
        nombre = self.tree.item(self.tree.selection())["values"][0]
        query = "DELETE FROM productos WHERE nomprod = ?"
        self.run_query(query,(nombre,))
        mb.showinfo("Información", "Eliminacion Correcta")
        self.get_productos()

    '''
    Función: editar_producto
    Propósito: crea una ventana emergente para ingresar los datos a modificar del producto
    '''
    def editar_producto(self):
        self.mensaje['text'] = ''
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError as e:
           
            mb.showinfo("Error", "Por favor selecciona un registro")
            return
        
        name = self.tree.item(self.tree.selection())['values'][0]
        old_price = self.tree.item(self.tree.selection())['values'][1]
        self.edit_wind = Toplevel(self)
        self.edit_wind.grab_set()
        self.edit_wind.transient()
        self.edit_wind.title("Editar Producto")
       
        Label(self.edit_wind, text = "Antiguo Nombre").grid(row = 0 , column = 1)
        Entry(self.edit_wind, textvariable =StringVar(self.edit_wind, value=name), state = "readonly").grid(row = 0 , column = 2)
       
        Label(self.edit_wind, text = "Nuevo Nombre").grid(row= 1, column =1)
        new_name=Entry(self.edit_wind,)
        new_name.grid(row = 1 , column = 2)
       
        Label(self.edit_wind, text = "Antiguo Precio").grid(row = 2 , column = 1)
        Entry(self.edit_wind, textvariable =StringVar(self.edit_wind, value=old_price), state = "readonly").grid(row = 2 , column = 2)
        
        Label(self.edit_wind, text = "Nuevo PRECIO").grid(row= 3, column =1)
        new_price=Entry(self.edit_wind)
        new_price.grid(row = 3 , column = 2)
        
        Button(self.edit_wind, text = 'Actualizar', command = lambda: self.edit_records(new_name.get(), name, 
                                        new_price.get(), old_price)).grid(row = 4, column = 2, sticky = W) 
    '''
    Función: edit_records
    Propósito: ejecuta la consulta en la BD para editar el registro del producto seleccionado
    '''
    def edit_records(self, new_name, name, new_price, old_price):
        query = 'UPDATE productos SET nomprod = ?,  costoprod = ? WHERE nomprod = ? AND costoprod = ?'
        parameters = (new_name, new_price,name, old_price)
        self.run_query(query, parameters)
        self.edit_wind.destroy()
        self.mensaje['text'] = 'Producto {} actualizado correctamente'.format(name)
        self.get_productos()

