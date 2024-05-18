from tkinter import *
import SGBD.verifications as v
from tkinter import messagebox
import mainWindow as mW
import change_password as cp

class VerifyEmailWindow(cp.UserActions):
    def __init__(self, user, password, root):
        super().__init__(user, password, root, "Verificar correo")
        self.root = root
        self.user = user
        self.password = password
        
        self.frame = Frame(self.root, width = 300, height = 400)
        self.frame.place(x = 0, y = 0)
        
        self.verifytext = Label(self.frame, text = "Introduce el correo", font = ("Arial", 16))
        self.verifytext.place(relx = 0.5, rely = 0.2, anchor=CENTER)
        
        self.entryemail = Entry(self.frame, font = ("Arial", 16))
        self.entryemail.place(relx = 0.5, rely = 0.3, anchor=CENTER)
        
        self.sendButton = Button(self.frame, text = "Enviar correo", 
            font = ("Arial", 16),command = self.send_email)
        
        self.sendButton.place(relx = 0.5, rely = 0.4, anchor=CENTER)
        
        self.codeMssg= Label(self.frame, text = "Código de verificación", font = ("Arial", 16))
        self.codeMssg.place(relx = 0.5, rely = 0.6, anchor=CENTER)
        
        self.entrycode = Entry(self.frame, font = ("Arial", 16))
        self.entrycode.place(relx = 0.5, rely = 0.7, anchor=CENTER)
        
        self.codeButton = Button(self.frame, text = "Verificar código",font = ("Arial", 16), command = self.verify_code)
        self.codeButton.place(relx = 0.5, rely = 0.8, anchor=CENTER)
        
        backtoMain = Button(self.frame, text = "Volver", font = ("Arial", 16), command = self.backtomain)
        backtoMain.place(relx = 0.5, rely = 0.9, anchor=CENTER)
        
        
    def send_email(self):
        self.email = self.entryemail.get()
        if self.email == '':
            messagebox.showerror("Error", "Introduce un correo")
            return
        try:
            self.code = v.send_mail(self.email, "Verificación de correo")
        except:
            messagebox.showerror("Error", "Introduce un correo válido")
            return
        
    def verify_code(self):
        try:
            if int(self.entrycode.get()) == self.code:
                v.verify_email(self.user, self.email)
                messagebox.showinfo('Correcto', 'Correo verificado')
                self.root.withdraw()
                new_root = Toplevel(self.root)
                mW.MainWindow(self.user, self.password, new_root)
                new_root.protocol("WM_DELETE_WINDOW", self.on_closing)
                
            else:
                messagebox.showerror("Error", "Código incorrecto")
        except Exception as e:
            messagebox.showerror("Error", str(e))
            
    def backtomain(self):
        self.root.withdraw()
        new_root = Toplevel(self.root)
        mW.MainWindow(self.user, self.password, new_root)
        new_root.protocol("WM_DELETE_WINDOW", self.on_closing)