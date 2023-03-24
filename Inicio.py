import sqlite3
import tkinter as tk
from tkinter import ttk, Frame
from tkinter import *
from VentanaNivel1 import Nivel1 as app1
from VentanaNivel2 import Nivel2 as app2
from VentanaNivel3 import Nivel3 as app3
from Usuarios import Usuarios as Uapp

class Inicio(Frame): 
    
    '''
    #Función: __init__ 
    #Propósito: permite que la clase almacene los datos de la GUI  
    '''    
    def __init__ (self,PantallaInicio):
        super().__init__(PantallaInicio)
        PantallaInicio.title("Inicio de Sesión")
        
        #Titulo de la interfaz        
        titulo = Label(PantallaInicio, text ="Sistema de Autenticación")
        titulo.place(x=120, y=70)

        #Label de indicaiones de datos
        descripcion = Label(PantallaInicio, text ="Ingrese su usuario y contraseña")
        descripcion.place(x=100, y=95)
        
        #Diseño UI       
        cuadro1 = LabelFrame(PantallaInicio, text = "Inicio de sesión")
        cuadro1.place(x=100, y=120, width=200, height=110)
        
        #Label usuario
        Label(cuadro1, text ="Usuario: ").grid(row=1, column=0)
        self.usuario = Entry(cuadro1)
        self.usuario.focus()
        self.usuario.grid(row =1, column =1)
        
        #Label contraseña
        Label(cuadro1, text ="Contraseña: ").grid(row=2, column=0)
        self.password = Entry(cuadro1, show = '*')
        self.password.grid(row =2, column =1)
        
        #Boton inicio de sesión
        ttk.Button(cuadro1,text= "Iniciar sesión", command=self.login).grid(row = 3, columnspan=2, sticky = W+E)
        
        #Mensajes de salida
        self.mensaje = Label(cuadro1,text="", fg="red")
        self.mensaje.grid(row=4, columnspan = 2, sticky = W+E)
        
    '''
    Función: validacionCampos y camposVacios
    Propósito: validar que los campos no se encuetran vacios a la hora de iniciar sesión o si solo uno se encuentra vacio
    '''

    def validacionCampos(self):
        return len(self.usuario.get()) == 0 or len(self.password.get()) ==0
    
    def camposVacios(self):
        return len(self.usuario.get()) == 0 and len(self.password.get()) == 0
    ''' 
    Función: login 
    Propósito: Valida que el usuario se encuentra en la base de datos
    Variables Involucradas: usuario, password
    '''
    def login(self):
        if self.camposVacios():
            self.mensaje["text"] = 'LLENAR LOS 2 CAMPOS'
        else:
            if self.validacionCampos():
                self.mensaje["text"] = 'FALTA LLENAR UN CAMPO'
                self.usuario.delete(0, END) #Limpia el campo del usuario.
                self.password.delete(0, END)# limpia el campo contraseña.
            else:
                
                while True:
                    password_criptText = Uapp.encriptar_claveLogin(None,self.password.get())
                    with sqlite3.connect('BDProyectoGr1.db') as db:
                        cursor = db.cursor()
                    buscarusu = ('SELECT * FROM Usuarios WHERE nomusu = ? AND clave = ?')
                    cursor.execute(buscarusu,[(self.usuario.get()),(password_criptText)])
                    results = cursor.fetchall()
                    
                    if results:
                        
                        encontrado = self.validarNivel(password_criptText)
                        if encontrado == 1:
                            self.mensaje["text"] = 'Bienvenido {}'.format(self.usuario.get())
                            self.usuario.delete(0, END) 
                            self.password.delete(0, END)
                            self.abrirVentana1()
                            break
                     
                        elif encontrado == 2:                            
                            self.mensaje["text"] = 'Bienvenido {}'.format(self.usuario.get())
                            self.usuario.delete(0, END) 
                            self.password.delete(0, END)
                            self.abrirVentana2()
                            break
                        elif encontrado == 3:                           
                            self.mensaje["text"] = 'Bienvenido {}'.format(self.usuario.get())
                            self.usuario.delete(0, END) 
                            self.password.delete(0, END)
                            self.abrirVentana3()
                            break
                        else:
                            print('XD')
                            break
                    else:
                        self.mensaje["text"] = 'USUARIO NO ENCONTRADO'
                        self.usuario.delete(0, END) 
                        self.password.delete(0, END)
                        break
    '''   
    Función: validarNivel
    Propósito: Con base a la contraseña se obtiene el nivel del usuario
    Variables Involucradas: password
    '''
    def validarNivel(self,passwordCripted):
         while True:
            with sqlite3.connect('BDProyectoGr1.db') as db:
                cursor = db.cursor()
            buscarnivel = ('SELECT nivel FROM Usuarios WHERE clave = ?')
            cursor.execute(buscarnivel,[(passwordCripted)])
            results = cursor.fetchall()
            
            for record in results:
                nivel = record[0]
            return nivel
    '''
    Funcion: Abrir Ventana 1
    Propósito: Abre la ventana correspondiente al nivel del usuario
    '''    
    def abrirVentana1(self):        
        ventana1 = tk.Toplevel()
        ventana1.grab_set()
        ventana1.transient()
        menu1 = app1(ventana1)

    '''
    Funcion: Abrir Ventana 2
    Propósito: Abre la ventana correspondiente al nivel del usuario
    '''         
    def abrirVentana2(self):        
        ventana2 = tk.Toplevel()
        ventana2.grab_set()
        ventana2.transient()
        menu2 = app2(ventana2)
        
    '''
    Funcion: Abrir Ventana 3
    Propósito: Abre la ventana correspondiente al nivel del usuario
    '''    
    def abrirVentana3(self):        
        ventana3 = tk.Toplevel()
        ventana3.grab_set()
        ventana3.transient()
        menu3 = app3(ventana3)

    '''
    Funcion: Abrir Ventana Inventarios
    Propósito: Abre la ventana correspondiente a la ventanas temporales
    '''    
    def abrirVentanaInventarios(self):        
        ventanaI = tk.Toplevel()
        ventanaI.grab_set()
        ventanaI.transient()
        menuI = appI(ventanaI)

'''
Inicialización de la GUI
'''
PantallaInicio = Tk()
PantallaInicio.geometry("400x400")
aplicacion = Inicio(PantallaInicio)
aplicacion.mainloop()


