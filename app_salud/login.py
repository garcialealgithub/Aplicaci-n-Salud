from tkinter import *
from tkinter import messagebox
import app_salud.SGBD.database_functions as BD
import app_salud.mainWindow as mW
import re

# Clase pre ventana. Representa una ventana de la aplicación de inicio de sesión o  registro
class preWindow:
    def __init__(self, root, title):
        self.root = root
        self.root.title(title)
        self.root.geometry("600x600")
        self.root.resizable(0, 0)
        self.bag = PhotoImage(file="app_salud/images/background.png")
        
        self.icon = PhotoImage(file="app_salud/images/icon.png")
        self.root.iconphoto(True, self.icon)

    def on_closing(self):
        self.root.destroy()

class Login(preWindow):
    def __init__(self, root):
        super().__init__(root, "Inicio de sesión")
        
        background = Label(self.root, image=self.bag)
        background.place(x=0, y=0, relwidth=1, relheight=1)

        frameLogin = Frame(self.root, width=270, height=360, bg="white", relief='ridge', border=8)
        frameLogin.place(relx=0.5, rely=0.5, anchor=CENTER)

        userTxt = Label(frameLogin, text="Usuario:", font=("Arial", 14))
        userTxt.place(relx=0.5, rely=0.2, anchor=CENTER)

        self.user_entry = Entry(frameLogin, font=("Arial", 12), justify="center")
        self.user_entry.place(relx=0.5, rely=0.3, anchor=CENTER)

        passwordTxt = Label(frameLogin, text="Contraseña:", font=("Arial", 14))
        passwordTxt.place(relx=0.5, rely=0.45, anchor=CENTER)

        self.passw_entry = Entry(frameLogin, font=("Arial", 14), justify="center", show="*")
        self.passw_entry.place(relx=0.5, rely=0.55, anchor=CENTER)

        loginButton = Button(frameLogin, text="Iniciar sesión", font=("Arial", 16), bg="red", fg="white", command=self.login)
        loginButton.place(relx=0.5, rely=0.7, anchor=CENTER)

        registerButton = Button(frameLogin, text="Registrarse", font=("Arial", 12), fg='black', command=self.register)
        registerButton.place(relx=0.5, rely=0.85, anchor=CENTER)



    def login(self):
        try:
            self.user = self.user_entry.get()
            self.password = self.passw_entry.get()
            if BD.comprobar_hash(self.password, BD.password_verification(usuario=self.user)):
                
                self.root.withdraw()
                new_root = Toplevel(self.root)
                mainWindow = mW.MainWindow(self.user, self.password, 'Rojo', new_root)
                new_root.protocol("WM_DELETE_WINDOW", self.on_closing)
                
            else:
                messagebox.showerror("Error", "Usuario o contraseña incorrectos")
        except Exception as e:
            messagebox.showerror("Error", 'Problema al iniciar sesión')   
            

    def register(self):
        self.root.withdraw()
        new_root = Toplevel(self.root)
        register = Register(new_root)
        new_root.protocol("WM_DELETE_WINDOW", self.on_closing)
        

class Register(preWindow):
    def __init__(self, root):
        super().__init__(root, "Registro")

        
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

        registerButton = Button(frameRegister, text="Registrarse", font=("Arial", 16), fg='white', bg='red', command=self.register)
        registerButton.place(relx=0.53, rely=0.9, anchor='e')

        loginButton = Button(frameRegister, text="Iniciar sesión", font=("Arial", 12), command=self.login)
        loginButton.place(relx=0.57, rely=0.9, anchor='w')


    def login(self):
        self.root.withdraw()
        new_root = Toplevel(self.root)
        login = Login(new_root)
        new_root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def register(self):
        try:
            self.usuario = self.Ruser_entry.get()
            self.contraseña = self.Rpassw_entry.get()

            # Intentar convertir la edad a un entero
            try:
                self.edad = int(self.Redad_entry.get())
            except ValueError:
                messagebox.showerror("Error", "La edad debe ser un número")
                return

            # Validar la contraseña con expresiones regulares
            if not re.match(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$', self.contraseña):
                messagebox.showerror("Error", "La contraseña debe tener al menos 8 caracteres, incluyendo al menos una letra y un número")
                return

            # Hashear la contraseña si pasa la validación
            hashed_password = BD.hasher(self.contraseña)

            if BD.add_security_table_row(self.usuario, password=hashed_password, age=self.edad, sex=self.sexo, email=None, everification=0):
                messagebox.showinfo("Correcto", "Usuario registrado correctamente")
        except Exception as e:
            messagebox.showerror("Error", str(e))