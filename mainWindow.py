from tkinter import *
import login as login
import SGBD.verifications as v
import verify_email_window as vw

## Clase ventana principal. Representa la ventana principal del programa
class MainWindow:
    def __init__(self, user, password, root):
        self.root = root
        self.root.title("Aplicación de salud")
        self.root.geometry("800x600")
        self.root.resizable(width=False, height=False)

        # Imágenes
        self.Mbg = PhotoImage(file="images/main_bg.png")
        self.userImg = PhotoImage(file="images/userImg.png")

        # Parámetros de ventana de usuario
        self.usuario = user
        self.password = password

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
        
        ## Botones de la ventana de usuario ##
        # ERROR aparente: no se puede poner un boton con menos height de 2 o tamaño de letra menor a 15
        # el mac cambia el estilo y no funciona. 
        
        def logout():
            self.root.withdraw()
            new_root = Toplevel(self.root)
            login.Login(new_root)
            new_root.protocol("WM_DELETE_WINDOW", self.on_closing)
            
        
        def verifyEmail():
            self.root.withdraw()
            new_root = Toplevel(self.root)
            vw.VerifyEmailWindow(self.usuario, self.password, new_root)
            new_root.protocol("WM_DELETE_WINDOW", self.on_closing)

        
        # Boton de verificar correo #
        verf = v.email_verificated(user)
        
        
        if not verf:
            verifyEmailButton = Button(self.userframe, text="Verificar correo", font=("Arial", 13), bg="gray", fg="black", command=verifyEmail)
            verifyEmailButton.place(relx=0.5, rely=0.6, anchor=CENTER)
        
        logoutButton = Button(self.userframe, text="Cerrar sesión", font=("Arial", 13), bg="gray", fg="black", command=logout)
        logoutButton.place(relx=0.5, rely=0.7, anchor=CENTER)
        
        boton1 = Button(self.userframe, text="no se", font=("Arial", 13), bg="gray", fg="black")
        boton1.place(relx=0.5, rely=0.8, anchor=CENTER)
        
        deleteAccountButton = Button(self.userframe, text="Eliminar ceunte", font=("Arial", 13), bg="gray", fg="black")
        deleteAccountButton.place(relx=0.5, rely=0.9, anchor=CENTER)
        
        self.pantalla = Frame(self.framePrincipal, width=608, height=450, relief='groove', border=8)
        self.pantalla.place(x=0, y=0)

        fondo = Label(self.pantalla, image=self.Mbg)
        fondo.place(x=0, y=0, relwidth=1, relheight=1)


        ## Botones de la ventana principal ##     
        self.buttons = Frame(self.framePrincipal, width=800, height=150, bg='gray')
        self.buttons.place(x=0, y=450)
        
        self.button2 = Button(self.buttons, text="Botón 2", width=10, height=2)
        self.button2.grid(column=2, row=0, pady=60, padx=54)

        self.button3 = Button(self.buttons, text="Botón 3", width=10, height=2)
        self.button3.grid(column=3, row=0, pady=60, padx=54)

        self.button4 = Button(self.buttons, text="Botón 4", width=10, height=2)
        self.button4.grid(column=4, row=0, pady=60, padx=54)

        self.button5 = Button(self.buttons, text="Botón 5", width=10, height=2)
        self.button5.grid(column=5, row=0, pady=60, padx=54)

    def on_closing(self):
        self.root.destroy()