from tkinter import *
import SGBD.verifications as v
from tkinter import messagebox
import mainWindow as mW
import SGBD.base_datos as BD

# Clase que representa la ventana de cambio de contraseña o verificación de correo
class UserActions:
    def __init__(self, user, password, root, title):
        self.user = user
        self.password = password
        self.root = root
        self.root.title(title)
        self.root.geometry("300x400")
        
    # Función que cierra la ventana
    def on_closing(self):
        self.root.destroy()        
        
        
# Clase para ventana de cambio de contraseña
class ChangePassword(UserActions):
    def __init__(self, user, password, root):
        super().__init__(user, password, root, "Cambiar contraseña")
        self.user = user
        self.password = password
        self.root = root
        
        self.frame = Frame(self.root, width = 300, height = 400)
        self.frame.place(x = 0, y = 0)
        
        # Botones y entradas de datos #
        self.verifytext = Label(self.frame, text = "Introduce el código \n que te hemos enviado al correo",     font = ("Arial", 16))
        self.verifytext.place(relx = 0.5, rely = 0.15, anchor=CENTER)
        
        self.entryCode = Entry(self.frame, font = ("Arial", 16))
        self.entryCode.place(relx = 0.5, rely = 0.25, anchor=CENTER)
        
        self.passw1 = Label(self.frame, text = "Introduce la nueva contraseña", font = ("Arial", 16))
        self.passw1.place(relx = 0.5, rely = 0.37, anchor=CENTER)
        
        self.entryPassw1 = Entry(self.frame, font = ("Arial", 15))
        self.entryPassw1.place(relx = 0.5, rely = 0.45, anchor=CENTER)
        
        self.passw2 = Label(self.frame, text = "Repite la nueva contraseña", font = ("Arial", 16))
        self.passw2.place(relx = 0.5, rely = 0.57, anchor=CENTER)
        
        self.entryPassw2 = Entry(self.frame, font = ("Arial", 15))
        self.entryPassw2.place(relx = 0.5, rely = 0.65, anchor=CENTER)
        
        self.changeButton = Button(self.frame, text = "Cambiar contraseña", font = ("Arial", 16), 
                    bg ='red', command=     self.change_password)
        self.changeButton.place(relx = 0.5, rely = 0.8, anchor=CENTER)
        
        backtoMain = Button(self.frame, text = "Volver", font = ("Arial", 16), command = self.backtomain)
        backtoMain.place(relx = 0.5, rely = 0.9, anchor=CENTER)
    
        # Enviamos el correo con el código de verificación
        self.code = v.send_mail(BD.saber_email(self.user), 'Cambio de contraseña')
            
    
    def change_password(self):
        
        try:
            self.EntryCode = self.entryCode.get()
            self.passw1 = self.entryPassw1.get()
            self.passw2 = self.entryPassw2.get()
            
            if self.passw1 == self.passw2:
                if  int(self.code) == int(self.code):
                    if BD.change_password(self.user, self.passw1):
                        messagebox.showinfo("Correcto", "Contraseña cambiada")
                        
                        self.root.withdraw()
                        new_root = Toplevel(self.root)
                        mW.MainWindow(self.user, self.passw1, new_root)
                        new_root.protocol("WM_DELETE_WINDOW", self.on_closing)
                    else:
                        messagebox.showerror("Error", "No se ha podido cambiar la contraseña")
                else:
                    messagebox.showerror("Error", "Código incorrecto")
            else:
                messagebox.showerror("Error", "Las contraseñas no coinciden")
                
        except Exception as e:
            messagebox.showerror("Error",e)
            
            
    def backtomain(self):
        self.root.withdraw()
        new_root = Toplevel()
        mW.MainWindow(self.user, self.password, new_root)
        new_root.protocol("WM_DELETE_WINDOW", self.on_closing)