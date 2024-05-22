from tkinter import *

def on_select(event):
    # Obtener el widget Listbox
    listbox = event.widget
    # Obtener el índice del elemento seleccionado
    index = listbox.curselection()
    # Obtener el valor del elemento seleccionado
    if index:
        value = listbox.get(index[0])
        print("Elemento seleccionado:", value)

root = Tk()
root.title("API")

caca = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# Crear una instancia de StringVar
list_var = StringVar(value=caca)

# Crear el Listbox y asociarlo con list_var
listbox = Listbox(root, listvariable=list_var, selectmode=SINGLE)
listbox.pack()

# Asociar la función de devolución de llamada al evento de selección
listbox.bind("<<ListboxSelect>>", on_select)

root.mainloop()
