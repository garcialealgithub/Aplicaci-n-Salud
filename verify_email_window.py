from tkinter import *
import SGBD.verifications as v
from tkinter import messagebox
import mainWindow as mW
import sys

class VerifyEmailWindow:
    def __init__(self, user, password, root):
        self.root = root
        self.root.title("Verificar correo")
        self.root.geometry("200x300")
        self.user = user
        self.password = password
        
        self.frame = Frame(self.root, width = 200, height = 300)
        self.frame.place(x = 0, y = 0)
        
        self.verifytext = Label(self.frame, text = "Introduce el correo", font = ("Arial", 12))
        self.verifytext.place(relx = 0.5, rely = 0.2, anchor=CENTER)
        
        self.entryemail = Entry(self.frame, font = ("Arial", 12))
        self.entryemail.place(relx = 0.5, rely = 0.3, anchor=CENTER)
        
        self.sendButton = Button(self.frame, text = "Enviar correo de verificación", 
            font = ("Arial", 15),command = self.send_email)
        
        self.sendButton.place(relx = 0.5, rely = 0.4, anchor=CENTER)
        
        self.codeMssg= Label(self.frame, text = "Código de verificación", font = ("Arial", 12))
        self.codeMssg.place(relx = 0.5, rely = 0.6, anchor=CENTER)
        
        self.entrycode = Entry(self.frame, font = ("Arial", 12))
        self.entrycode.place(relx = 0.5, rely = 0.7, anchor=CENTER)
        
        self.codeButton = Button(self.frame, text = "Verificar código",font = ("Arial", 15), command = self.verify_code)
        self.codeButton.place(relx = 0.5, rely = 0.8, anchor=CENTER)
        
        self.root.mainloop()
    
    def send_email(self):
        self.email = self.entryemail.get()
        if self.email == '':
            messagebox.showerror("Error", "Introduce un correo")
            return
        self.code = v.send_mail(self.entryemail.get(), "Verificación de correo")
        
    def on_closing(self):
        self.root.destroy()
        
    def verify_code(self):
        try:
            self.email = self.entryemail.get()
            print(self.user, self.password)
            v.verify_email(self.user, self.email)
            messagebox.showinfo('Correcto', 'Correo verificado')
            self.root.withdraw()
            new_root = Toplevel(self.root)
            mW.MainWindow(self.user, self.password, new_root)
            new_root.protocol("WM_DELETE_WINDOW", self.on_closing)
                
        except Exception as e:
            messagebox.showerror("Error", str(e))
            
""" def verify_code(self):
        try:
            if self.entrycode.get() == self.code:
                print(self.user, self.email, self.code)
                v.verify_email(self.user, self.email)
                messagebox.showinfo('Correcto', 'Correo verificado')
                self.root.withdraw()
                new_root = Toplevel(self.root)
                mW.MainWindow(self.user, self.password, new_root)
                new_root.protocol("WM_DELETE_WINDOW", self.on_closing)
                
            else:
                messagebox.showerror("Error", "Código incorrecto")
        except Exception as e:
            messagebox.showerror("Error", str(e))"""
    