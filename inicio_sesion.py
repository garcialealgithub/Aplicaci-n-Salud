from tkinter import *

root = Tk()
root.title("Inicio de sesión")
root.geometry("600x600")
root.resizable(0,0)
bag = PhotoImage(file="background.png")
icon = PhotoImage(file="icon.png")
root.iconphoto(False, icon)

background = Label(root, image=bag)
background.place(x=0, y=0, relwidth=1, relheight=1)

frameLogin = Frame(root, width=270, height=360, bg="white", relief="raised", bd=5)
frameLogin.place(relx = 0.5, rely = 0.5, anchor = CENTER)

user = Label(frameLogin, text="Usuario:", font=("Arial", 18))
user.place(relx = 0.5, rely = 0.2, anchor = CENTER)

user_entry = Entry(frameLogin, font=("password", 18), justify="center")
user_entry.place(relx = 0.5, rely = 0.3, anchor = CENTER)


password = Label(frameLogin, text="Contraseña:", font=("Arial", 18))
password.place(relx = 0.5, rely = 0.45, anchor = CENTER)

passw_entry = Entry(frameLogin, font=("Arial", 18), justify="center", show="*")
passw_entry.place(relx = 0.5, rely = 0.55, anchor = CENTER)

def login():
        user = user_entry.get()
        password = passw_entry.get()
        if user == "admin" and password == "admin":
                print("Bienvenido")
        else:
                print("Usuario o contraseña incorrectos")
                
loginButton = Button(frameLogin, text="Iniciar sesión", font=("Arial", 18), bg="blue", fg="black", command=login)
loginButton.place(relx = 0.5, rely = 0.7, anchor = CENTER)


                
root.mainloop()