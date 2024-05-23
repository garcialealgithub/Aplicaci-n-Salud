from tkinter import *
import app_salud.SGBD.verifications as v
from tkinter import messagebox
import app_salud.mainWindow as mW
import app_salud.change_password as cp

class VerifyEmailWindow(cp.UserActions):
    def __init__(self, user, password, color, root):
        super().__init__(user, password, color, root, "Verify email")
        
        
        self.frame = Frame(self.root, width = 300, height = 400)
        self.frame.place(x = 0, y = 0)
        
        self.verifytext = Label(self.frame, text = "Entry code", font = ("Arial", 16))
        self.verifytext.place(relx = 0.5, rely = 0.2, anchor=CENTER)
        
        self.entryemail = Entry(self.frame, font = ("Arial", 16))
        self.entryemail.place(relx = 0.5, rely = 0.3, anchor=CENTER)
        
        self.sendButton = Button(self.frame, text = "Send mail", 
            font = ("Arial", 16),command = self.send_email)
        
        self.sendButton.place(relx = 0.5, rely = 0.4, anchor=CENTER)
        
        self.codeMssg= Label(self.frame, text = "Code", font = ("Arial", 16))
        self.codeMssg.place(relx = 0.5, rely = 0.6, anchor=CENTER)
        
        self.entrycode = Entry(self.frame, font = ("Arial", 16))
        self.entrycode.place(relx = 0.5, rely = 0.7, anchor=CENTER)
        
        self.codeButton = Button(self.frame, text = "Verify",font = ("Arial", 15), command = self.verify_code)
        self.codeButton.place(relx = 0.5, rely = 0.8, anchor=CENTER)
        
        backtoMain = Button(self.frame, text = "Back", font = ("Arial", 14), command = self.backtomain)
        backtoMain.place(relx = 0.5, rely = 0.9, anchor=CENTER)
        
        
    def send_email(self):
        self.email = self.entryemail.get()
        if self.email == '':
            messagebox.showerror("Error", "Type a email")
            return
        try:
            self.code = v.send_mail(self.email, "Verificación de correo")
        except:
            messagebox.showerror("Error", "Enter a valid email")
            return
        
    def verify_code(self):
        try:
            if int(self.entrycode.get()) == int(self.code):
                v.verify_email(self.user, self.email)
                messagebox.showinfo('Correcto', 'Email verificated')
                self.backtomain()
                
            else:
                messagebox.showerror("Error", "Invalid code")
        except Exception as e:
            messagebox.showerror("Error", str(e))
            
    def backtomain(self):
        self.root.withdraw()
        new_root = Toplevel(self.root)
        mW.MainWindow(self.user, self.password, self.color, new_root)
        new_root.protocol("WM_DELETE_WINDOW", self.on_closing)