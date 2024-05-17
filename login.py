from tkinter import *
import tkinter as tk
from tkinter import messagebox
import SGBD.base_datos as BD
import mainWindow as mW

# Clase pre ventana. Representa una ventana de la aplicación de inicio de sesión o  registro
class preWindow:
    def __init__(self, root, title):
        self.root = root
        self.root.title(title)
        self.root.geometry("600x600")
        self.root.resizable(0, 0)
        
        self.icon = PhotoImage(file="images/icon.png")
        self.root.iconphoto(True, self.icon)

    def on_closing(self):
        self.root.destroy()

class Login(preWindow):
    def __init__(self, root):
        super().__init__(root, "Inicio de sesión")
        self.bag = PhotoImage(file="images/background.png")
        background = Label(self.root, image=self.bag)
        background.place(x=0, y=0, relwidth=1, relheight=1)

        frameLogin = Frame(self.root, width=270, height=360, bg="white", relief='ridge', border=8)
        frameLogin.place(relx=0.5, rely=0.5, anchor=CENTER)

        user = Label(frameLogin, text="Usuario:", font=("Arial", 14))
        user.place(relx=0.5, rely=0.2, anchor=CENTER)

        self.user_entry = Entry(frameLogin, font=("Arial", 12), justify="center")
        self.user_entry.place(relx=0.5, rely=0.3, anchor=CENTER)

        password = Label(frameLogin, text="Contraseña:", font=("Arial", 14))
        password.place(relx=0.5, rely=0.45, anchor=CENTER)

        self.passw_entry = Entry(frameLogin, font=("Arial", 14), justify="center", show="*")
        self.passw_entry.place(relx=0.5, rely=0.55, anchor=CENTER)

        loginButton = Button(frameLogin, text="Iniciar sesión", font=("Arial", 16), bg="red", fg="white", command=self.login)
        loginButton.place(relx=0.5, rely=0.7, anchor=CENTER)

        registerButton = Button(frameLogin, text="Registrarse", font=("Arial", 12), fg='black', command=self.register)
        registerButton.place(relx=0.5, rely=0.85, anchor=CENTER)



    def login(self):
        user = self.user_entry.get()
        password = self.passw_entry.get()
        if BD.comprobar_hash(password, BD.password_verification(usuario=user)):
            
            self.root.withdraw()
            new_root = Toplevel(self.root)
            mainWindow = mW.MainWindow(user, password, new_root)
            new_root.protocol("WM_DELETE_WINDOW", self.on_closing)

        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

    def register(self):
        self.root.withdraw()
        new_root = Toplevel(self.root)
        register = Register(new_root)
        new_root.protocol("WM_DELETE_WINDOW", self.on_closing)
        

class Register(preWindow):
    def __init__(self, root):
        super().__init__(root, "Registro")

        self.bag = PhotoImage(file="images/background.png")
        background = Label(self.root, image=self.bag)
        background.place(x=0, y=0, relwidth=1, relheight=1)

        frameRegister = Frame(self.root, width=270, height=360, relief='ridge', border=8)
        frameRegister.place(relx=0.5, rely=0.5, anchor=CENTER)

        Ruser = Label(frameRegister, text="Usuario:", font=("Arial", 14))
        Ruser.place(relx=0.2, rely=0.1)

        self.Ruser_entry = Entry(frameRegister, font=("Arial", 12), justify="center")
        self.Ruser_entry.place(relx=0.5, rely=0.2, anchor=CENTER)

        Rpassword = Label(frameRegister, text="Contraseña:", font=("Arial", 14))
        Rpassword.place(relx=0.2, rely=0.3)

        self.Rpassw_entry = Entry(frameRegister, font=("Arial", 12), justify="center", show="*")
        self.Rpassw_entry.place(relx=0.5, rely=0.4, anchor=CENTER)

        Rpassword = Label(frameRegister, text="Edad:", font=("Arial", 14))
        Rpassword.place(relx=0.2, rely=0.5)

        self.Redad_entry = Entry(frameRegister, font=("Arial", 12), justify="center")
        self.Redad_entry.place(relx=0.5, rely=0.6, anchor=CENTER)

        sexo = Label(frameRegister, text="Sexo:", font=("Arial", 14))
        sexo.place(relx=0.2, rely=0.7)

        self.variable = StringVar()
        self.sexo = ''

        def sexChoose():
            self.sexo = self.variable.get()

        hombre = Radiobutton(frameRegister, text="Hombre", variable=self.variable, value='M', command=sexChoose)
        hombre.place(relx=0.5, rely=0.70, anchor='w')
        mujer = Radiobutton(frameRegister, text="Mujer", variable=self.variable, value='F', command=sexChoose)
        mujer.place(relx=0.5, rely=0.78, anchor='w')

        registerButton = Button(frameRegister, text="Registrarse", font=("Arial", 16), fg='white', bg='red', command=self.register_user)
        registerButton.place(relx=0.53, rely=0.9, anchor='e')

        loginButton = Button(frameRegister, text="Iniciar sesión", font=("Arial", 12), command=self.login)
        loginButton.place(relx=0.57, rely=0.9, anchor='w')


    def login(self):
        self.root.withdraw()
        new_root = Toplevel(self.root)
        login = Login(new_root)
        new_root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def register_user(self):
        usuario = self.Ruser_entry.get()
        contraseña = self.Rpassw_entry.get()
        edad = self.Redad_entry.get()
        sexo = self.sexo

        BD.insert_user_info(usuario, BD.hasher(contraseña), edad, sexo)
        messagebox.showinfo("Correcto", "Usuario registrado correctamente")

