from tkinter import *
from tkinter import ttk
import app_salud.login as login
import app_salud.SGBD.verifications as verf
import app_salud.verify_email_window as verfWindow
import app_salud.change_password as cp
import app_salud.SGBD.database_functions as BD
import app_salud.graphconfig as gconfig
import app_salud.api as api



## Clase ventana principal. Representa la ventana principal del programa
class MainWindow:
    def __init__(self, user, password, color, root):
        self.root = root
        self.root.title("Aplicación de salud")
        self.root.geometry("800x600")
        self.root.resizable(width=False, height=False)
        
        # Imágenes
        self.Mbg = PhotoImage(file="app_salud/images/main_bg.png")
        self.userImg = PhotoImage(file="app_salud/images/userImg.png")
        self.confImg = PhotoImage(file="app_salud/images/configuration.png")

        # Parámetros de ventana de usuario
        self.usuario = user
        self.password = password
        self.color = color
        print(self.color)
        self.modo_ejercicios = False
        self.seleccion = None
        
        # Frame principal
        self.framePrincipal = Frame(self.root, width=800, height=600)
        self.framePrincipal.place(x=0, y=0)

        ## Frame del usuario ##
        self.userframe = Frame(self.framePrincipal, width=200, height=450, relief='groove', border=8)
        self.userframe.place(x=600, y=0) 
        
        self.user = Label(self.userframe, text="Bienvenido, ", font=("Arial", 14))
        self.user.place(relx=0.5, rely=0.40, anchor=CENTER)

        self.user = Label(self.userframe, text=user, font=("Arial", 14), fg='red')
        self.user.place(relx=0.5, rely=0.45, anchor=CENTER)
        
        self.userImg = Label(self.userframe, image=self.userImg)
        self.userImg.place(relx=0.5, rely=0.2, anchor=CENTER)
        
        ## Botones de la ventana de usuario
        
        # Botones que solo aparecen si el correo está verificado
        if not verf.email_verificated(user):
            verifyEmailButton = Button(self.userframe, text="Verificar correo", font=("Arial", 13), bg="gray", 
                fg="black", command=self.verifyEmail)
            verifyEmailButton.place(relx=0.5, rely=0.6, anchor=CENTER)
        
        else:
            self.changePasswButton = Button(self.userframe, text="Cambiar contraseña", font=("Arial", 13), 
                bg="gray", fg="black", command=self.changePassword)
            self.changePasswButton.place(relx=0.5, rely=0.8, anchor=CENTER)
        
        self.logoutButton = Button(self.userframe, text="Cerrar sesión", font=("Arial", 13), bg="gray", 
            fg="black", command=self.logout)
        self.logoutButton.place(relx=0.5, rely=0.7, anchor=CENTER)
        
        self.deleteAccountButton = Button(self.userframe, text="Eliminar cuenta", font=("Arial", 13), 
            bg="gray", fg="black", command=self.deleteAccount)
        self.deleteAccountButton.place(relx=0.5, rely=0.9, anchor=CENTER)
        
        
        # Frame de la pantalla principal
        self.pantalla = Frame(self.framePrincipal, width=608, height=450, relief='groove', border=8)
        self.pantalla.place(x=0, y=0)

        self.fondo = Label(self.pantalla, image=self.Mbg)
        self.fondo.place(x=0, y=0, relwidth=1, relheight=1)


        ## Botones de la ventana principal ## 
        self.buttons = Frame(self.framePrincipal, width=800, height=150, bg='gray')
        self.buttons.place(x=0, y=450)
        
        self.confButton = Button(self.buttons, image=self.confImg, command=self.graphConfig)
        self.confButton.place(x=0, y=0)

        self.button2 = Button(self.buttons, text="Botón 2", width=10, height=2)
        self.button2.grid(column=2, row=0, pady=60, padx=60)

        self.button3 = Button(self.buttons, text="Botón 3", width=10, height=2)
        self.button3.grid(column=3, row=0, pady=60, padx=60)

        self.button4 = Button(self.buttons, text="Botón 4", width=10, height=2)
        self.button4.grid(column=4, row=0, pady=60, padx=60)

        self.button5 = Button(self.buttons, text="Botón 5", width=10, height=2, command=self.verEjercicios)
        self.button5.grid(column=5, row=0, pady=60, padx=60)
    

    ## Funciones de los botones ##
    def logout(self):
        self.root.withdraw()
        new_root = Toplevel(self.root)
        login.Login(new_root)
        new_root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        
    def graphConfig(self):
        self.root.withdraw()
        new_root = Toplevel(self.root)
        gconfig.grapConfig(self.usuario, self.password, self.color, new_root, "Configuración de color")
        new_root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def deleteAccount(self):
        BD.drop_user_info(self.usuario)
        
        self.root.withdraw()
        new_root = Toplevel(self.root)
        login.Login(new_root)
        new_root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def changePassword(self):
        self.root.withdraw()
        new_root = Toplevel(self.root)
        cp.ChangePassword(self.usuario, self.password, self.color, new_root)
        new_root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        
    def verifyEmail(self):
        self.root.withdraw()
        new_root = Toplevel(self.root)
        verfWindow.VerifyEmailWindow(self.usuario, self.password, self.color, new_root)
        new_root.protocol("WM_DELETE_WINDOW", self.on_closing)
            
    # Función de cierre de ventana
    def on_closing(self):
        self.root.destroy()
    
    def verEjercicios(self):
        self.modo_ejercicios = True
        self.actualizar_interfaz()

    def mandar_seleccion(self, event):
        self.respuesta = api.InfoEjercicios(self.seleccion.get())
        
    
    def actualizar_interfaz(self):
        if self.modo_ejercicios:
            # Si estamos en modo ejercicios, muestra el Combobox
            if self.seleccion is None:  # Solo crea si no existe
                self.seleccion = ttk.Combobox(self.root, values=api.musculos, state='readonly')
                self.seleccion.place(x=8, y=8)
                self.seleccion.bind("<<ComboboxSelected>>", self.mandar_seleccion)
                
            self.fondo.lower()  # Manda el fondo a la capa inferior
        else:
            # Si no estamos en modo ejercicios, asegúrate de que el fondo esté visible
            self.fondo.lift()  # Manda el fondo a la capa superior
            if self.seleccion is not None:
                self.seleccion.pack_forget()  # Oculta el Combobox
                self.seleccion = None  # Resetea el Combobox a None
