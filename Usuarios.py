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
class Usuarios(Frame):    
    '''
    Función: __init__ 
    Propósito: permite que la clase almacene los datos de la GUI  
    '''
    def __init__(self, master= None):
        super().__init__(master)
        self.master = master
        master.title("Administrar usuarios")        
        
        #Crea el frame
        self.frame = LabelFrame(master, text ="Registrar un nuevo usuario")
        self.frame.grid(row = 0, column =0, columnspan = 3, pady = 20 )
        
        #Ingreso del Usuario
        self.lblnomusu = Label(self.frame,text ="Nombre usuario").grid(row = 1 , column =0) # texto a mostrar
        self.nomusu = Entry(self.frame) 
        self.nomusu.grid(row=1, column =1) # ingresar texto

        #Ingreso del password
        self.lblclave = Label(self.frame,text ="clave").grid(row = 2 , column =0) # texto a mostrar
        self.clave = Entry(self.frame) 
        self.clave.grid(row=2, column =1) 
    
        #Ingreso del nivel de usuario
        self.lblnivel = Label(self.frame,text ="nivel").grid(row = 3 , column =0) # texto a mostrar
        self.nivel = Entry(self.frame) 
        self.nivel.grid(row=3, column= 1) 

        #Botones de la interfaz
        self.btnregistrar =ttk.Button(self.frame, text = "Registrar", command = self.add_usuario).grid(row=4,columnspan =2,sticky=W+E)
        self.btnborrar = ttk.Button(master,text = "Eliminar usuario", command = self.borrar_usuario).grid(row = 5 , columnspan = 2, sticky = W+E)
        
        #Mensaje 
        self.mensaje = Label(master,text="", fg="RED")
        self.mensaje.grid(row=3, column=0, columnspan = 2 , sticky = W+E)

        # Tabla
        self.tree = ttk.Treeview(master,height=10, columns = 3)
        self.tree.grid(row= 4,column=0 , columnspan = 2)
        self.tree["columns"]=("#1","#2")        
        
        self.tree.heading("#0", text = "Usuario",anchor = CENTER)
        self.tree.heading("#1", text = "Clave",anchor = CENTER)
        self.tree.heading("#2", text = "Nivel",anchor = CENTER)
        self.get_usuarios()
        
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
    Función: get_usuarios 
    Propósito: Limpia la tabla y obtiene la lista de usuarios de la BD.  
    ''' 
    def get_usuarios(self):
        #Limpia la tabla
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        #Consultar los datos  
        query="SELECT*FROM Usuarios ORDER BY nivel DESC"
        db_rows = self.run_query(query)
        for row in db_rows:
            self.tree.insert("",0,text= row[0], values = (row[1],row[2]))        
    '''
    Función: validacion
    Propósito: valida que los campos del registro del usuario no estén vacios.
    '''          
    def validacion(self):
        return len(self.nomusu.get())!=0 and len(self.clave.get())!= 0 and len(self.nivel.get()) !=0 
    
    '''
    Función: encriptar_claveLogin
    Propósito: recupera la clave del login y la encripta para ser buscada en la BD
    '''
    def encriptar_claveLogin(self, password):
        passwordEncriptado = StringVar()
        password_cript = ''
        passwordEncriptado = sha1(password.encode('utf-8')).hexdigest()
        password_cript =  passwordEncriptado
        
        return password_cript
    
    '''        
    Función: encriptar_clave
    Propósito: encriptar la clave del usuario en el registro por medio de la libreria hashlib
    ''' 
    def encriptar_clave(self):
        claveEncriptada = StringVar()
        clave_cript = ''
        claveEncriptada = sha1(self.clave.get().encode('utf-8')).hexdigest()
        clave_cript = claveEncriptada
        
        return clave_cript
    
    '''
    Función: add_usuario
    Propósito: Ejecuta la consulta para Registrar un usuario en la BD    
    '''
    def add_usuario(self):
        try:
            if self.validacion():
                clave_criptText = self.encriptar_clave()
                query = 'INSERT INTO Usuarios VALUES(?, ?, ?,NULL)'
                parameters =  (self.nomusu.get(),clave_criptText, self.nivel.get(),)
                self.run_query(query, parameters)
                mb.showinfo("Información", "Los datos fueron cargados")
                self.mensaje['text'] = 'Usuario {} ha sido agregado satisfactoriamente'.format(self.nomusu.get())
                self.nomusu.delete(0, END)
                self.clave.delete(0, END)
                self.nivel.delete(0, END)
            else:
                mb.showinfo("Informacion","Llenar los campos correspondientes")
            self.get_usuarios()
        except sqlite3.IntegrityError as e:
            mb.showinfo("Información", "Intente nuevamente")
        self.nomusu.delete(0, END)
        self.clave.delete(0, END)
        self.nivel.delete(0, END)
        self.get_usuarios()
        
    '''
    Función: borrar_Usuario
    Propósito: ejecuta la consulta para eliminar un usuario de la BD
    '''  
    def borrar_usuario(self):
        try:
            self.tree.item(self.tree.selection())["text"]
        except IndexError as e:
            mb.showinfo("Error", "Por favor selecciona un registro")
            return
        nombre = self.tree.item(self.tree.selection())["text"]
        query = "DELETE FROM Usuarios WHERE nomusu = ?"
        self.run_query(query,(nombre,))
        mb.showinfo("Información", "Información eliminada correctamente.")
        self.get_usuarios()
