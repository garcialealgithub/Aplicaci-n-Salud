from tkinter import *

class Login:
        def __init__(self, root):
                self.root = root
                self.root.title("Inicio de sesión")
                self.root.geometry("600x600")
                self.root.resizable(0,0)
                self.bag = PhotoImage(file = "background.png")
                self.icon = PhotoImage(file = "icon.png")
                self.root.iconphoto(False, self.icon)

                background = Label(self.root, image = self.bag)
                background.place(x = 0, y = 0, relwidth = 1, relheight = 1)

                frameLogin = Frame(self.root, width = 270, height=360, bg = "white", relief = 'ridge', border=8)
                frameLogin.place(relx = 0.5, rely = 0.5, anchor = CENTER)

                user = Label(frameLogin, text = "Usuario:", font = ("Arial", 14))
                user.place(relx = 0.5, rely = 0.2, anchor = CENTER)

                self.user_entry = Entry(frameLogin, font = ("password", 12), justify = "center")
                self.user_entry.place(relx = 0.5, rely = 0.3, anchor = CENTER)


                password = Label(frameLogin, text = "Contraseña:", font = ("Arial", 14))
                password.place(relx = 0.5, rely = 0.45, anchor = CENTER)

                self.passw_entry = Entry(frameLogin, font=("Arial", 14), justify = "center", show = "*")
                self.passw_entry.place(relx = 0.5, rely = 0.55, anchor = CENTER)

                loginButton = Button(frameLogin, text="Iniciar sesión", font=("Arial", 16), bg = "red", fg = "white", command = self.login)
                loginButton.place(relx = 0.5, rely = 0.7, anchor = CENTER)

                registerButton = Button(frameLogin, text="Registrarse", font=("Arial", 12), fg = 'black', command = self.register)
                registerButton.place(relx = 0.5, rely = 0.85, anchor = CENTER)

        def login(self):
                # Aqui se debe implementar una excepcion para que no se pueda iniciar sesion si no se llenan todos los campos
                print(self.user_entry.get())
                print(self.passw_entry.get())
        
        def register(self):
                # Se cierra la ventana de inicio de sesion y se abre la ventana de registro
                register = Register(root)


class Register:
        def __init__(self, root):
                self.root = root
                self.root.title("Registro")
                
                frameRegister = Frame(self.root, width = 270, height=360, relief = 'ridge', border = 8)
                frameRegister.place(relx = 0.5, rely = 0.5, anchor = CENTER)


                Ruser = Label(frameRegister, text = "Usuario:", font = ("Arial", 14))
                Ruser.place(relx = 0.2, rely = 0.1)

                self.Ruser_entry = Entry(frameRegister, font = ("Arial", 12), justify = "center")
                self.Ruser_entry.place(relx = 0.5, rely = 0.2, anchor = CENTER)


                Rpassword = Label(frameRegister, text = "Contraseña:", font = ("Arial", 14))
                Rpassword.place(relx = 0.2, rely = 0.3)

                self.Rpassw_entry = Entry(frameRegister, font = ("Arial", 12), justify = "center")
                self.Rpassw_entry.place(relx = 0.5, rely = 0.4, anchor = CENTER)


                Rpassword = Label(frameRegister, text = "Edad:", font = ("Arial", 14))
                Rpassword.place(relx = 0.2, rely = 0.5)

                self.Redad_entry = Entry(frameRegister, font = ("Arial", 12), justify = "center")
                self.Redad_entry.place(relx = 0.5, rely = 0.6, anchor = CENTER)


                sexo = Label(frameRegister, text = "Sexo:", font = ("Arial", 14))
                sexo.place(relx = 0.2, rely = 0.7)

                self.variable = StringVar()
                self.sexo = ''

                def sexChoose():
                        self.sexo = self.variable.get()

                hombre = Radiobutton(frameRegister, text="Hombre", variable=self.variable, value='Hombre', command = sexChoose)
                hombre.place(relx=0.5, rely=0.70, anchor='w')
                mujer = Radiobutton(frameRegister, text="Mujer", variable=self.variable, value='Mujer', command = sexChoose)
                mujer.place(relx=0.5, rely=0.78, anchor='w')


                registerButton = Button(frameRegister, text = "Registrarse", font = ("Arial", 16), fg ='white', bg ='red', command = self.register)
                registerButton.place(relx = 0.53, rely = 0.9, anchor = 'e')

                loginButton = Button(frameRegister, text = "Iniciar sesión", font = ("Arial", 12), command=self.login)
                loginButton.place(relx = 0.57, rely = 0.9, anchor = 'w')


        def login(self):
                # Se cierra la ventana de registro y se abre la ventana de inicio de sesion
                login=Login(root)
        
        def register(self):
                # Al principio todas las variables estan vacias, debe implementarse una excepcion para que no se registre si no se llenan todos los campos
                # Estas variables se deben guardar ya que serán los datos básicos del usuario
                print(self.Ruser_entry.get())
                print(self.Rpassw_entry.get())
                print(self.Redad_entry.get())
                print(self.sexo)



if __name__ == "__main__":
        root = Tk()

        login = Login(root)
        
        root.mainloop()