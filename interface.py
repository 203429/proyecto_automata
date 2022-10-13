from tkinter import *
from tkinter import filedialog, messagebox
import main as m

tf_validate = False

def open_file():
    tf = open("./Reporte.txt")
    data = tf.read()
    txtarea.delete(1.0,END)
    txtarea.insert(END, data)
    tf.close()

def open_dir():
    global dirr;
    dirr = filedialog.askdirectory(title='Abrir carpeta ...', initialdir='/')
    pathh.insert(END, dirr)

def script(dirr):
    if m.main(dirr)==False:
        messagebox.showerror('ERROR','Directorio NO válido')
    else:
        m.main(dirr)
        open_file()


ws = Tk()
ws.title("Validador de importaciones")
ws.geometry("600x650")
ws['bg']='#C1C1C1'

txtarea = Text(ws, width=65, height=25)
txtarea.pack(pady=30)

pathh = Entry(ws)
pathh.pack(side=LEFT, expand=True, fill=X, padx=10)

dir_button = Button(
    ws, 
    text="Buscar Carpeta", 
    command=open_dir
    ).pack(side=RIGHT, expand=True, fill=X, padx=10)

val_button = Button(
    ws, 
    text="Validar", 
    command=lambda: script(dirr)
    ).pack(side=RIGHT, expand=True, fill=X, padx=10)

ws.mainloop()
# import tkinter as tk
# import tkinter.filedialog as fd
# from tkinter.ttk import LabelFrame
# from tkinter import *
# import main as m

# is_packed = False

# class Application(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.inicializar_gui()

#     def inicializar_gui(self):
#         self.title('Validador de importaciones')
#         self.geometry('1000x400')

#         txt_directory = tk.Label(self, text="Ruta del directorio: ")
#         txt_directory.pack(padx=60, pady=30)
#         txt_path = tk.Label(self, text="")
#         txt_path.pack(padx=60, pady=30)

#         btn_seleccionar_carpeta = tk.Button(self, text='Seleccionar carpeta...')
#         btn_seleccionar_carpeta['command'] = lambda: self.seleccionar_carpeta(txt_path)
#         btn_seleccionar_carpeta.pack(padx=60, pady=10)

#     def seleccionar_carpeta(self,txt_path):
#         global directorio;
#         global is_packed
#         directorio = fd.askdirectory(title='Abrir carpeta ...', initialdir='/')
#         if directorio:
#             txt_path.config(text = directorio)
#             btn_validar = tk.Button(self, text='Validar')
#             btn_validar['command'] = lambda: m.main(directorio)
#             if is_packed==False:
#                 is_packed=True
#                 btn_validar.pack(padx=60, pady=10)

# def main():
#     app = Application()
#     app.mainloop()

# if __name__ == '__main__':
#     main()