from tkinter import *
import tkinter as tk
import bcrypt

# Lista de contraseñas sin hashear
plain_passwords = {
    "Pepito": "a",
    "Paquito": "b",
    "Taron": "c",
    "a": "a"
}

# Diccionario de contraseñas hasheadas
hashed_passwords = {}

# Hashing de las contraseñas y almacenamiento en el diccionario de contraseñas hasheadas
for user, password in plain_passwords.items():
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    hashed_passwords[user] = hashed_password

class Window:
    def __init__(self, title):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry("600x600")
        self.root.resizable(0, 0)
        
        self.icon = PhotoImage(file="icon.png")
        self.root.iconphoto(True, self.icon)

    def destroy(self):
        self.root.destroy()

class Login(Window):
    def __init__(self):
        super().__init__("Inicio de sesión")
        self.bag = PhotoImage(file="background.png")
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

        self.root.mainloop()

    def login(self):
        user = self.user_entry.get()
        password = self.passw_entry.get()
        if user in hashed_passwords and bcrypt.checkpw(password.encode(), hashed_passwords[user]):
            print("Usuario encontrado")
            self.destroy()
            mainWindow = MainWindow(user)
        else:
            print("Usuario no encontrado")

    def register(self):
        self.destroy()
        register = Register()

class Register(Window):
    def __init__(self):
        super().__init__("Registro")

        self.bag = PhotoImage(file="background.png")
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

        hombre = Radiobutton(frameRegister, text="Hombre", variable=self.variable, value='Hombre', command=sexChoose)
        hombre.place(relx=0.5, rely=0.70, anchor='w')
        mujer = Radiobutton(frameRegister, text="Mujer", variable=self.variable, value='Mujer', command=sexChoose)
        mujer.place(relx=0.5, rely=0.78, anchor='w')

        registerButton = Button(frameRegister, text="Registrarse", font=("Arial", 16), fg='white', bg='red', command=self.register_user)
        registerButton.place(relx=0.53, rely=0.9, anchor='e')

        loginButton = Button(frameRegister, text="Iniciar sesión", font=("Arial", 12), command=self.login)
        loginButton.place(relx=0.57, rely=0.9, anchor='w')

        self.root.mainloop()

    def login(self):
        self.destroy()
        login = Login()

    def register_user(self):
        usuario = self.Ruser_entry.get()
        contraseña = self.Rpassw_entry.get()
        edad = self.Redad_entry.get()
        sexo = self.sexo
        
        # Guardar la contraseña sin hashear
        plain_passwords[usuario] = contraseña

        # Hashing de la contraseña
        hashed_password = bcrypt.hashpw(contraseña.encode(), bcrypt.gensalt())

        # Guardar la contraseña hasheada
        hashed_passwords[usuario] = hashed_password

        info_registro = [usuario, contraseña, edad, sexo]
        print("Usuario registrado:", info_registro)

class MainWindow:
    def __init__(self, user):
        self.root = Tk()
        self.root.title("Aplicación de salud")
        self.root.geometry("800x600")
        self.root.resizable(0, 0)

        Mbg = PhotoImage(file="main_bg.png")
        userImg = PhotoImage(file="userImg.png")

        self.usuario = user

        self.framePrincipal = Frame(self.root, width=800, height=600)
        self.framePrincipal.place(x=0, y=0)

        self.userframe = Frame(self.framePrincipal, width=200, height=450, relief='groove', border=8)
        self.userframe.place(x=600, y=0) 
        
        self.user = Label(self.userframe, text="Bienvenido, ", font=("Arial", 14))
        self.user.place(relx=0.5, rely=0.45, anchor=CENTER)

        self.user = Label(self.userframe, text=user, font=("Arial", 14), fg='red')
        self.user.place(relx=0.5, rely=0.55, anchor=CENTER)
        
        self.userImg = Label(self.userframe, image=userImg)
        self.userImg.place(relx=0.5, rely=0.2, anchor=CENTER)
        
        self.userFrameButtons = Frame(self.userframe, width=100, height=100)
        self.userFrameButtons.place(relx=0.5, rely=0.8, anchor=CENTER)

        changePw = Button(self.userFrameButtons, text="Cambiar contraseña", font=("Arial", 10))
        changePw.pack()

        logout = Button(self.userFrameButtons, text="Cerrar sesión", font=("Arial", 10))
        logout.pack()

        deleteAccount = Button(self.userFrameButtons, text="Eliminar cuenta", font=("Arial", 10))  
        deleteAccount.pack()

        self.pantalla = Frame(self.framePrincipal, width=608, height=450, relief='groove', border=8)
        self.pantalla.place(x=0, y=0)

        fondo = Label(self.pantalla, image=Mbg)
        fondo.place(x=0, y=0, relwidth=1, relheight=1)

        self.buttons = Frame(self.framePrincipal, width=800, height=150, bg='gray')
        self.buttons.place(x=0, y=450)

        self.button1 = tk.Button(self.buttons, text="Botón 1", width=10, height=2)
        self.button1.grid(column=1, row=0, pady=60, padx=54)

        self.button2 = tk.Button(self.buttons, text="Botón 2", width=10, height=2)
        self.button2.grid(column=2, row=0, pady=60, padx=54)

        self.button3 = tk.Button(self.buttons, text="Botón 3", width=10, height=2)
        self.button3.grid(column=3, row=0, pady=60, padx=54)

        self.button4 = tk.Button(self.buttons, text="Botón 4", width=10, height=2)
        self.button4.grid(column=4, row=0, pady=60, padx=54)

        self.button5 = tk.Button(self.buttons, text="Botón 5", width=10, height=2)
        self.button5.grid(column=5, row=0, pady=60, padx=54)

        self.root.mainloop()

if __name__ == "__main__":
    login = Login()

print(hashed_passwords)
