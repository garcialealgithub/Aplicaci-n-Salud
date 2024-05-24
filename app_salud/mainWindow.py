from tkinter import *
from tkinter import ttk
import app_salud.login as login
import app_salud.SGBD.verifications as verf
import app_salud.verify_email_window as verfWindow
import app_salud.change_password as cp
import app_salud.SGBD.database_functions as BD
import app_salud.graphconfig as gconfig
import app_salud.api as api
import app_salud.GRAFOS.grafos as graph
from PIL import Image


## Clase ventana principal. Representa la ventana principal del programa
class MainWindow:
    def __init__(self, user, password, color, root):
        self.root = root
        self.root.title("Health app")
        self.root.geometry("800x600")
        self.root.resizable(width=False, height=False)
        
        # Imágenes
        self.Mbg = PhotoImage(file="app_salud/images/main_bg.png")
        self.userImg = PhotoImage(file="app_salud/images/userImg.png")
        self.confImg = PhotoImage(file="app_salud/images/configuration.png")
        self.beginner = PhotoImage(file="app_salud/images/beginner.png")
        self.intermediate = PhotoImage(file="app_salud/images/intermediate.png")
        self.expert = PhotoImage(file="app_salud/images/expert.png")
        self.abdominals = PhotoImage(file="app_salud/images/abdominals.png")
        self.abductors = PhotoImage(file="app_salud/images/abductors.png")
        self.adductors = PhotoImage(file="app_salud/images/adductors.png")
        self.biceps = PhotoImage(file="app_salud/images/biceps.png")
        self.calves = PhotoImage(file="app_salud/images/calves.png")
        self.chest = PhotoImage(file="app_salud/images/chest.png")
        self.forearms = PhotoImage(file="app_salud/images/forearms.png")
        self.glutes = PhotoImage(file="app_salud/images/glutes.png")
        self.hamstrings = PhotoImage(file="app_salud/images/hamstrings.png")
        self.lats = PhotoImage(file="app_salud/images/lats.png")
        self.lower_back = PhotoImage(file="app_salud/images/lower_back.png")
        self.middle_back = PhotoImage(file="app_salud/images/middle_back.png")
        self.neck = PhotoImage(file="app_salud/images/neck.png")
        self.quadriceps = PhotoImage(file="app_salud/images/quadriceps.png")
        self.traps = PhotoImage(file="app_salud/images/traps.png")
        self.triceps = PhotoImage(file="app_salud/images/triceps.png")

        # Parámetros de ventana de usuario
        self.usuario = user
        self.password = password
        self.color = color
        self.modo_Pantalla = None
        self.seleccionEjercicio = self.ejercicios = self.seleccionGrafo = None
        self.nombresEjercicios = StringVar(value=[])
        self.diasDisponibles = StringVar(value=[])
        
        # Frame principal
        self.framePrincipal = Frame(self.root, width=800, height=600)
        self.framePrincipal.place(x=0, y=0)

        ## Frame del usuario ##
    
        self.userframe = Frame(self.framePrincipal, width=200, height=450, relief='groove', border=8)
        self.userframe.place(x=600, y=0) 
        
        self.userImg = Label(self.userframe, image=self.userImg)
        self.userImg.place(relx=0.5, rely=0.2, anchor=CENTER)

        self.user = Label(self.userframe, text="Welcome, ", font=("Arial", 14))
        self.user.place(relx=0.5, rely=0.40, anchor=CENTER)

        self.user = Label(self.userframe, text=user, font=("Arial", 14), fg='red')
        self.user.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        
        
        ## Botones de la ventana de usuario
        
        # Botones que solo aparecen si el correo está verificado
        if not verf.email_verificated(user):
            verifyEmailButton = Button(self.userframe, text="Verify email", font=("Arial", 13), bg="gray", 
                fg="black", command=self.verifyEmail)
            verifyEmailButton.place(relx=0.5, rely=0.6, anchor=CENTER)
        
        else:
            self.changePasswButton = Button(self.userframe, text="Change password", font=("Arial", 13), 
                bg="gray", fg="black", command=self.changePassword)
            self.changePasswButton.place(relx=0.5, rely=0.8, anchor=CENTER)
        
        self.logoutButton = Button(self.userframe, text="Log out", font=("Arial", 13), bg="gray", 
            fg="black", command=self.logout)
        self.logoutButton.place(relx=0.5, rely=0.7, anchor=CENTER)
        
        self.deleteAccountButton = Button(self.userframe, text="Delete account", font=("Arial", 13), 
            bg="gray", fg="black", command=self.deleteAccount)
        self.deleteAccountButton.place(relx=0.5, rely=0.9, anchor=CENTER)
        
        
        # Frame de la pantalla principal
        self.pantalla = Frame(self.framePrincipal, width=608, height=450, relief='groove', border=8)
        self.pantalla.place(x=0, y=0)

        self.fondo = Label(self.pantalla, image=self.Mbg)
        self.fondo.place(x=0, y=0, relwidth=1, relheight=1)


        ## Botones de la ventana principal ## 
        self.buttons = Frame(self.framePrincipal, width=800, height=150, bg='gray')
        self.buttons.place(x=0, y=450)
        
        self.confButton = Button(self.buttons, image=self.confImg, command=self.graphConfig)
        self.confButton.place(x=0, y=0)

        
        self.button3 = Button(self.buttons, text="Graphs", width=10, height=2, command=self.graphVisualize)
        self.button3.grid(column=0, row=0, pady=60, padx=94)

        self.button4 = Button(self.buttons, text="Clean", width=10, height=2, command=self.limpiarPantalla)
        self.button4.grid(column=1, row=0, pady=60, padx=94)

        self.button5 = Button(self.buttons, text="Exercises", width=10, height=2, command=self.verEjercicios)
        self.button5.grid(column=2, row=0, pady=60, padx=94)
    

    ## Funciones de los botones ##
    def limpiarPantalla(self):
        self.fondo.lift()
        self.modo_Pantalla = None
        self.actualizar_interfaz()

    def logout(self):
        self.root.withdraw()
        new_root = Toplevel(self.root)
        login.Login(new_root)
        new_root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        
    def graphConfig(self):
        self.root.withdraw()
        new_root = Toplevel(self.root)
        gconfig.grapConfig(self.usuario, self.password, self.color, new_root, "Color configuration")
        new_root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def deleteAccount(self):
        BD.drop_user(self.usuario)
        
        self.root.withdraw()
        new_root = Toplevel(self.root)
        login.Login(new_root)
        new_root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def changePassword(self):
        self.root.withdraw()
        new_root = Toplevel(self.root)
        cp.ChangePassword(self.usuario, self.password, self.color, new_root)
        new_root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        
    def verifyEmail(self):
        self.root.withdraw()
        new_root = Toplevel(self.root)
        verfWindow.VerifyEmailWindow(self.usuario, self.password, self.color, new_root)
        new_root.protocol("WM_DELETE_WINDOW", self.on_closing)
            
    # Función de cierre de ventana
    def on_closing(self):
        self.root.destroy()
    


    # Funciones para selección de ejercicios
    def verEjercicios(self):
        self.limpiarPantalla()
        self.modo_Pantalla = 'ejercicios'
        self.actualizar_interfaz()

    def mandar_seleccionEjercicio(self, event):
        self.respuesta = api.InfoEjercicios(self.seleccion.get())
        self.nombresEjercicios = StringVar(value = api.nombresEjercicios(self.respuesta))
        self.actualizar_interfaz()
        

    def visualizacion_ejercicios(self):
        
        self.miniatura = Frame(self.pantalla, width=178, height=204, relief='groove', border=8)
        self.miniatura.place(x=0, y=230)

        self.dificultadTexto = Label(self.miniatura, text="Dificultad:", font=("Arial", 12))
        self.dificultadTexto.place(x=0, rely=0.1)

        self.dificultad = self.informacion_ejercicios['difficulty']
        match self.dificultad:
            case 'beginner':
                self.una_estrella = Label(self.miniatura, image=self.beginner)
                self.una_estrella.place(x=2, rely=0.1)
            case 'intermediate':
                self.dos_estrella = Label(self.miniatura, image=self.intermediate)
                self.dos_estrella.place(x=2, rely=0.1)
            case 'expert':
                self.tres_estrella = Label(self.miniatura, image=self.expert)
                self.tres_estrella.place(x=2, rely=0.1)
        
        self.muscle = self.informacion_ejercicios['muscle']
        match self.muscle:
            case 'abdominals':
                self.abdominals_widge = Label(self.miniatura, image=self.abdominals)
                self.abdominals_widge.place(x=20, rely=0.4)
            case 'abductors':
                self.abductors_widge = Label(self.miniatura, image=self.abductors)
                self.abductors_widge.place(x=20, rely=0.4)
            case 'adductors':
                self.adductors_widge = Label(self.miniatura, image=self.adductors)
                self.adductors_widge.place(x=20, rely=0.4)
            case 'biceps':
                self.biceps_widge = Label(self.miniatura, image=self.biceps)
                self.biceps_widge.place(x=20, rely=0.4)
            case 'calves':
                self.calves_widge = Label(self.miniatura, image=self.calves)
                self.calves_widge.place(x=20, rely=0.4)
            case 'chest':
                self.chest_widge = Label(self.miniatura, image=self.chest)
                self.chest_widge.place(x=20, rely=0.4)
            case 'forearms':
                self.forearms_widge = Label(self.miniatura, image=self.forearms)
                self.forearms_widge.place(x=20, rely=0.4)
            case 'glutes':
                self.glutes_widge = Label(self.miniatura, image=self.glutes)
                self.glutes_widge.place(x=20, rely=0.4)
            case 'hamstrings':
                self.hamstrings_widge = Label(self.miniatura, image=self.hamstrings)
                self.hamstrings_widge.place(x=20, rely=0.4)
            case 'lats':
                self.lats_widge = Label(self.miniatura, image=self.lats)
                self.lats_widge.place(x=20, rely=0.4)
            case 'lower_back':
                self.lower_back_widge = Label(self.miniatura, image=self.lower_back)
                self.lower_back_widge.place(x=20, rely=0.4)
            case 'middle_back':
                self.middle_back_widge = Label(self.miniatura, image=self.middle_back)
                self.middle_back_widge.place(x=20, rely=0.4)
            case 'neck':
                self.neck_widge = Label(self.miniatura, image=self.neck)
                self.neck_widge.place(x=20, rely=0.4)
            case 'quadriceps':
                self.quadriceps_widge = Label(self.miniatura, image=self.quadriceps)
                self.quadriceps_widge.place(x=20, rely=0.4)
            case 'traps':
                self.traps_widge = Label(self.miniatura, image=self.traps)
                self.traps_widge.place(x=20, rely=0.4)
            case 'triceps':
                self.triceps_widge = Label(self.miniatura, image=self.triceps)
                self.triceps_widge.place(x=20, rely=0.4)

        self.mainInfo = Frame(self.pantalla, width=415, height=434, relief='groove', border=8)
        self.mainInfo.place(x=178, y=0)

        self.title = Label(self.mainInfo, text=self.ejercicio, font=("Arial", 17))
        self.title.place(relx=0.5, rely=0.05, anchor=CENTER)

        self.tipo = self.informacion_ejercicios['type']
        self.equipamiento = self.informacion_ejercicios['equipment']
        self.parrafo = self.informacion_ejercicios['instructions']

        self.type = Label(self.mainInfo, text=f"Tipo: {self.tipo}", font=("Arial", 12))
        self.type.place(x=0.3, rely=0.1, anchor=W)

        self.equipment = Label(self.mainInfo, text=f"Equipamiento: {self.equipamiento}", font=("Arial", 12))
        self.equipment.place(relx=0.9, rely=0.1, anchor=E)

        self.titulo = Label(self.mainInfo, text="Instrucciones:", font=("Arial", 12))
        self.titulo.place(relx=0.5, rely=0.18, anchor=CENTER)
        self.instruccion = Label(self.mainInfo, text=self.parrafo, font=("Arial", 9), wraplength=375, justify=CENTER)
        self.instruccion.place(relx=0.03, rely=0.2)

    def on_select(self, event):
        # Obtener el widget Listbox
        self.seleccion2 = event.widget
        # Obtener el Ãndice del elemento seleccionado
        index = self.seleccion2.curselection()
        # Obtener el valor del elemento seleccionado
        if index:
            
            self.ejercicio = self.seleccion2.get(index[0])
            self.informacion_ejercicios = api.concrete_exercise(self.respuesta, index[0])
            self.visualizacion_ejercicios()
        

    # Funciones para selección de graficos
    def graphVisualize(self):
        self.limpiarPantalla()
        self.modo_Pantalla = 'graphs'
        self.actualizar_interfaz()

    def print_graph(self, event):
        self.limpiarPantalla()
        self.grafo_a_imprimir = self.seleccionGrafo.get()
        match self.grafo_a_imprimir:
            case 'Peso':
                graph.grafico_peso(self.usuario, '2024-05-16', 7, self.color)
                try:
                    self.labelgrafo.destroy()
                except:
                    pass
                self.img=PhotoImage(file='app_salud/GRAFOS/images/grafico_peso.png')
                self.labelgrafo = Label(self.pantalla, image=self.img)
                self.labelgrafo.place(x=65, y=10)
                
            case 'Pasos':

                graph.grafico_pasos(self.usuario, '2024-05-16', 7, self.color)
                try:
                    self.labelgrafo.destroy()
                except:
                    pass
                self.img=PhotoImage(file='app_salud/GRAFOS/grafos_images/pasos/pasos_grafico.png')
                self.labelgrafo = Label(self.pantalla, image=self.img)
                self.labelgrafo.place(x=65, y=10)

            case 'F. Cardíaca':
                graph.grafico_freq_card(self.usuario, '2024-05-16', 7, self.color)
                try:
                    self.labelgrafo.destroy()
                except:
                    pass
                self.img=PhotoImage(file='app_salud/GRAFOS/grafos_images/freq_card/freq_card_grafico.png')
                self.labelgrafo = Label(self.pantalla, image=self.img)
                self.labelgrafo.place(x=65, y=10)
                

            case 'Sueño':
                graph.grafico_sueño(self.usuario, '2024-05-16', 7)
                try:
                    self.labelgrafo.destroy()
                except:
                    pass
                self.img=PhotoImage(file='app_salud/GRAFOS/grafos_images/sueño/sueño_grafico.png')
                self.labelgrafo = Label(self.pantalla, image=self.img)
                self.labelgrafo.place(x=65, y=10)
            
            case 'Entrenamiento':
                graph.grafico_entrenamiento(self.usuario, '2024-05-16', 7)
                try:
                    self.labelgrafo.destroy()
                except:
                    pass
                self.img=PhotoImage(file='app_salud/GRAFOS/grafos_images/entreno/entreno_grafico.png')
                self.labelgrafo = Label(self.pantalla, image=self.img)
                self.labelgrafo.place(x=65, y=10)
  
 



    def actualizar_interfaz(self):
        
        self.ComboFrame = Frame(self.pantalla, relief='groove', border=8, width=178, height=230)
        self.ComboFrame.place(x=0, y=0)
                   
        match self.modo_Pantalla:
            case 'ejercicios':
                try:
                    self.labelgrafo.destroy()
                except:
                     pass
                # Si estamos en modo ejercicios, muestra el Combobox
                self.seleccion = ttk.Combobox(self.ComboFrame, values=api.musculos, state='readonly')
                self.seleccion.place(x=8, y=8)
                self.seleccion.bind("<<ComboboxSelected>>", self.mandar_seleccionEjercicio)
          
                self.seleccion2 = Listbox(self.ComboFrame, listvariable=self.nombresEjercicios)
                self.seleccion2.place(x=8, y=30)
                self.seleccion2.bind("<<ListboxSelect>>", self.on_select)
                self.fondo.lower()  # Manda el fondo a la capa inferior

            case 'graphs':
                try:
                    self.mainInfo.destroy()
                    self.miniatura.destroy()
                except:
                    pass
                
                self.seleccionGrafo = ttk.Combobox(self.ComboFrame, values=graph.tipografo, state='readonly')
                self.seleccionGrafo.place(x=8, y=8)
                self.seleccionGrafo.bind("<<ComboboxSelected>>", self.print_graph)

            case None:
                try:
                    self.ComboFrame.destroy()
                    self.mainInfo.destroy()
                    self.miniatura.destroy()
                    self.labelgrafo.destroy()
                except:
                    pass
                self.fondo.lift() # Manda el fondo a la capa superior
