import os
from tkinter import Canvas, filedialog
from PIL import Image
import tkinter
from tkinter import PhotoImage, ttk
import customtkinter
import tkinter.messagebox as tkmb
from CTkTable import *

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
       
        self.geometry("200x300")
        self.title("ProjectUp")
        # Icono de la ventana
        absolutepath = os.path.abspath(__file__)
        Directorio = os.path.dirname(absolutepath)
        path = Directorio + r'/img/icon.png'	
        icon = PhotoImage(file=path)
        self.wm_iconphoto(True, icon)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.my_frame = LoginFrame(master=self)
        self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        
class LoginFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        
        self.label = customtkinter.CTkLabel(self, text='Inicio de sesión')
        self.label.grid(pady=12, padx=10)

        self.user_entry = customtkinter.CTkEntry(
            self, placeholder_text="Usuario"
        )
        self.user_entry.grid(pady=12, padx=10)

        self.user_pass = customtkinter.CTkEntry(
            self, placeholder_text="Contraseña", show="*")
        self.user_pass.grid(pady=12, padx=10)

        self.button = customtkinter.CTkButton(
            self, text='Iniciar sesión', command=self.login
        )
        self.button.grid(pady=12, padx=10)

    def login(self):
        username = self.user_entry.get()
        password = self.user_pass.get()
        username = "PM-201907343"
        password = "123"
        if username == "PM-201907343" and password == "123":
            tkmb.showinfo(title='Inicio de sesión exitoso',
                          message='Binvenido '+username)

            self.master.title('ProjectUp - Admin')
            self.master.geometry('700x500')

            self.master.my_frame.destroy()
            self.master.my_frame = MainFrame(master=self.master)
            self.master.my_frame.grid(padx=20, pady=20, sticky='nsew')
        else:
            tkmb.showerror('Error', 'Usuario o contraseña incorrectos')


class MainFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.AgregarEmpleados = []
        self.label = customtkinter.CTkLabel(self, text='Administrador')
        self.label.grid(row=0, column=0, pady=12, padx=10)

        self.button = customtkinter.CTkButton(
            self, text='Cerrar sesión', command=self.logout)
        self.button.grid(row=0, column=1, pady=12, padx=10)

        self.tabview = customtkinter.CTkTabview(self, width=740, height=490)
        self.tabview.grid(row=1, column=0, columnspan=2, pady=12, padx=10)

        self.tab_1 = self.tabview.add("Empleados")
        self.EmployeeTab()
        self.tab_2 = self.tabview.add("Proyectos y tareas")
        self.ProjectAndTaskTab()        

    def EmployeeTab(self):
        self.btn_carga_empleados = customtkinter.CTkButton(
            self.tab_1, text='Carga masiva de empleados', command=self.carga_empleados
        )
        self.btn_carga_empleados.grid(row=0, column=0, pady=12, padx=10)

        
        
    def carga_empleados(self):
        ruta_proyecto = os.getcwd()
        ruta_archivo = filedialog.askopenfilename(initialdir=ruta_proyecto, title="Seleccionar archivo")
        empleados = []
        with open(ruta_archivo, "r") as f:
            for linea in f:
                valores = linea.strip().split(",")
                empleado = [
                    valores[0].strip(),
                    valores[1].strip(),
                    valores[2].strip(),
                    valores[3].strip()
                ]
                empleados.append(empleado)

        # Convertir la lista de empleados a una cadena en formato Python
        self.values = "[\n"
        for empleado in empleados:
            self.values += f"    {empleado},\n"
        self.values += "]"

        self.AgregarEmpleados = self.values
        if len(self.AgregarEmpleados) > 0:
            self.table_empleados = CTkTable(self.tab_1, values=list(eval(self.AgregarEmpleados)))
            self.table_empleados.grid(row=1, column=0, pady=12, padx=10)
            print("La lista de empleados a agregar tiene datos adentro")
        else:
            values = [
                    ["ID", "Nombre", "Constraseña", "Puesto"]
            ]
            self.table_empleados = CTkTable(self.tab_1, values=values)
            self.table_empleados.grid(row=1, column=0, pady=12, padx=10)
            print("La lista de empleados a agregar está vacía") 


    def ProjectAndTaskTab(self):
        self.btn_load_json = customtkinter.CTkButton(
            self.tab_2, text="Cargar JSON")
        self.btn_load_json.grid(row=0, column=0, pady=12, padx=10)

        self.btn_project_report = customtkinter.CTkButton(
            self.tab_2, text="Reporte de proyectos")
        self.btn_project_report.grid(row=0, column=1, pady=12, padx=10)

        self.btn_task_report = customtkinter.CTkButton(
            self.tab_2, text="Reporte de tareas")
        self.btn_task_report.grid(row=0, column=2, pady=12, padx=10)

        self.btn_optionmenu = customtkinter.CTkOptionMenu(
            self.tab_2, values=["Opcion 1", "Opcion 2", "Opcion 3"], command=self.optionmenu_callback)
        self.btn_optionmenu.grid(row=0, column=3, pady=12, padx=10)
        self.btn_optionmenu.set("Opcion 1")

        self.treeview = ttk.Treeview(self.tab_2, height=15, show='tree')
        self.treeview.place(relx=0.01, rely=0.1, width=500, height=500)
        self.treeview.insert('', 2, 'i2', text='Python')
        self.treeview.insert('', 0, 'i0', text='CustomTk')
        self.treeview.insert('', 1, 'i1', text='Tk')
        self.treeview.insert('i2', 'end', text='Texto aleatorio 1 para ve como se ve')
        self.treeview.insert('i2', 'end', text='Label')
        self.treeview.insert('i0', 'end', text='Dummy nivel 1')

    def optionmenu_callback(self, choice):
        tkmb.showinfo(title='Opción seleccionada', message=choice)

    def logout(self):
        self.master.title("ProjectUp")
        self.master.geometry('200x300')

        self.master.my_frame.destroy()
        self.master.my_frame = LoginFrame(master=self.master)
        self.master.my_frame.grid(
            row=0, column=0, padx=20, pady=20, sticky="nsew")

app = App()
app.mainloop()
