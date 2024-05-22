from tkinter import *
import app_salud.SGBD.verifications as v
from tkinter import messagebox
import app_salud.mainWindow as mW
import app_salud.SGBD.database_functions as BD
import re

# Clase que representa la ventana de cambio de contraseña o verificación de correo
class UserActions:
    def __init__(self, user, password, color, root, title):
        self.user = user
        self.password = password
        self.root = root
        self.color = color
        self.root.title(title)
        self.root.geometry("300x400")
        
    # Función que cierra la ventana
    def on_closing(self):
        self.root.destroy()        

# Clase para ventana de cambio de contraseña
class ChangePassword(UserActions):
    def __init__(self, user, password, color, root):
        super().__init__(user, password, color, root, "Cambiar contraseña")
        
        self.frame = Frame(self.root, width=300, height=400)
        self.frame.place(x=0, y=0)
        
        # Botones y entradas de datos #
        self.verifytext = Label(self.frame, text="Introduce el código \n que te hemos enviado al correo", font=("Arial", 15))
        self.verifytext.place(relx=0.5, rely=0.15, anchor=CENTER)
        
        self.entryCode = Entry(self.frame, font=("Arial", 16))
        self.entryCode.place(relx=0.5, rely=0.25, anchor=CENTER)
        
        self.passw1 = Label(self.frame, text="Introduce la nueva contraseña", font=("Arial", 15))
        self.passw1.place(relx=0.5, rely=0.37, anchor=CENTER)
        
        self.entryPassw1 = Entry(self.frame, font=("Arial", 15), show='*')
        self.entryPassw1.place(relx=0.5, rely=0.45, anchor=CENTER)
        
        self.passw2 = Label(self.frame, text="Repite la nueva contraseña", font=("Arial", 15))
        self.passw2.place(relx=0.5, rely=0.57, anchor=CENTER)
        
        self.entryPassw2 = Entry(self.frame, font=("Arial", 15), show='*')
        self.entryPassw2.place(relx=0.5, rely=0.65, anchor=CENTER)
        
        self.changeButton = Button(self.frame, text="Cambiar contraseña", font=("Arial", 15), bg='red', fg='white', command=self.change_password)
        self.changeButton.place(relx=0.5, rely=0.8, anchor=CENTER)
        
        backtoMain = Button(self.frame, text="Volver",  font=("Arial", 15), command=self.backtomain)
        backtoMain.place(relx=0.5, rely=0.9, anchor=CENTER)
    
        # Enviamos el correo con el código de verificación
        self.code = v.send_mail(BD.get_email_by_user(self.user), 'Cambio de contraseña')


    def backtomain(self):
        self.root.withdraw()
        new_root = Toplevel()
        mW.MainWindow(self.user, self.new_password1, self.color, new_root)
        new_root.protocol("WM_DELETE_WINDOW", self.on_closing)
        

    def change_password(self):
        try:
            entry_code = self.entryCode.get()
            self.new_password1 = self.entryPassw1.get()
            self.new_password2 = self.entryPassw2.get()
            
            # Expresiones regulares para validación
            code_pattern = re.compile(r'^\d{6}$')  # Código de verificación de 6 dígitos
            password_pattern = re.compile(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$')  # Contraseña con al menos 8 caracteres, una letra y un número
            
            if self.new_password1 == self.new_password2:
                if code_pattern.match(entry_code):
                    if password_pattern.match(self.new_password1):
                        if int(entry_code) == int(self.code):
                            if BD.update_security_table_row(user=self.user, password=BD.hasher(self.new_password1), database='app_salud/SGBD/database.db'):
                                messagebox.showinfo("Correcto", "Contraseña cambiada")
                                self.backtomain()
                            else:
                                messagebox.showerror("Error", "No se ha podido cambiar la contraseña")
                        else:
                            messagebox.showerror("Error", "Código incorrecto")
                    else:
                        messagebox.showerror("Error", "La contraseña debe tener al menos 8 caracteres, incluir una letra y un número")
                else:
                    messagebox.showerror("Error", "Código de verificación inválido")
            else:
                messagebox.showerror("Error", "Las contraseñas no coinciden")
        except Exception as e:
            messagebox.showerror("Error", str(e))
            
    
