import binascii
import json
from tkinter import *
from tkinter import filedialog	
import tkinter.messagebox
import os
from tkinter.ttk import Combobox, Notebook, Treeview
import webbrowser
from tkinter import Tk

from ArbolAvl import *

ListaEmpleados = []
ListaTareas = []

class MyApp:
	def __init__(self):
		# Creando ventana principal
		self.ventana_login = Tk()
		self.ventana_login.title("Login")
		self.ventana_login.config(bg="skyblue")
		# Icono de la ventana
		absolutepath = os.path.abspath(__file__)
		Directorio = os.path.dirname(absolutepath)
		path = Directorio + r'/img/icon.png'	
		icon = PhotoImage(file=path)
		self.ventana_login.wm_iconphoto(True, icon)

		## Objetos de la ventana principal login
		# Cuadro de texto para el usuario
		usuariolabel = Label(self.ventana_login,text="Usuario:")
		usuariolabel.grid(row=1, column=1, sticky="w", padx=10, pady=10)
		
		self.usuario_entry = Entry(self.ventana_login)
		self.usuario_entry.insert(0, "PM-201907343")
		self.usuario_entry.grid(row=1, column=2, sticky="w", padx=10, pady=10)
		
		# Cuadro de texto para la contraseña
		contrasena_label = Label(self.ventana_login, text="Contraseña:")
		contrasena_label.grid(row=2, column=1, sticky="w", padx=10, pady=10)

		self.contrasena_entry = Entry(self.ventana_login, show="*") 
		self.contrasena_entry.insert(0, "123")
		self.contrasena_entry.grid(row=2, column=2, sticky="w", padx=10, pady=10)
		
		# Boton de login
		login_button = Button(self.ventana_login, text="Iniciar sesión", command=self.verificar_login)
		login_button.grid(row=3, column=2, sticky="w", padx=10, pady=10)
		
		## Objetos de la ventana Admin PM-201907343
		self.ventana_admin = Toplevel(self.ventana_login)
		self.ventana_admin.title("Administrador")
		self.ventana_admin.withdraw()

		# Crear un Frame para el Label y la imagen
		self.frame = Frame(self.ventana_admin)
		self.frame.grid(row=0, column=0, sticky="w")

		# Crear un Label con el texto "PM-201907343"
		self.label = Label(self.frame, text="PM-201907343", font=("Arial", 20, "bold"))
		self.label.grid(row=0, column=0, sticky="e")

		# Cargar la imagen y redimensionarla
		absolutepath = os.path.abspath(__file__)
		Directorio = os.path.dirname(absolutepath)
		path = Directorio + r'/img/admin.png'
		self.imagen = PhotoImage(file=path).subsample(8)

		# Crear un Label con la imagen
		self.imagen_label = Label(self.frame, image=self.imagen)
		self.imagen_label.grid(row=0, column=2, sticky="e")

		# Crear un botón
		self.SalirAdmin = Button(self.frame, text="Cerrar Sesión", font=("Arial", 16, "bold"), bg="red", fg="white", command=self.CerrarSesionAdmin)
		self.SalirAdmin.grid(row=0, column=3, sticky="w")

		# Crear el widget Notebook
		self.notebook = Notebook(self.ventana_admin)
		self.notebook.grid(row=1, column=0, sticky="nsew")

		# Crear la primera pestaña con una tabla
		self.tab1 = Frame(self.notebook)
		self.notebook.add(self.tab1, text="Empleados")

		# Boton Carga de Archivo .csv
		cargarArchivo = Button(self.tab1, text="Cargar .csv", command=self.AgregarEmpleados, font=("Arial", 16, "bold"), bg="blue", fg="white")
		cargarArchivo.grid(row=2, column=0, sticky="w", padx=10, pady=10)

		# Crear la self.tablaEmpleados
		self.tablaEmpleados = Treeview(self.tab1, columns=("id","nombre","contraseña","puesto","index"))
		self.tablaEmpleados.heading("id", text="Id")
		self.tablaEmpleados.heading("nombre", text="Nombre")
		self.tablaEmpleados.heading("contraseña", text="Contraseña")
		self.tablaEmpleados.heading("puesto", text="Puesto")
		self.tablaEmpleados.heading("index", text="Index")
		self.tablaEmpleados["show"] = "headings"
		self.tablaEmpleados.grid(row=4, column=0, sticky="nsew", padx=10, pady=10, columnspan=2, rowspan=2)

		# Crear la segunda pestaña con un recuadro de texto multilinea
		self.tab2 = Frame(self.notebook)
		self.notebook.add(self.tab2, text="Proyectos y tareas")

		# Boton Carga de Archivo .Json
		cargarArchivo = Button(self.tab2, text="Cargar .json", command=self.cargar_json, font=("Arial", 16, "bold"), bg="black", fg="white")
		cargarArchivo.grid(row=2, column=0, sticky="w", padx=10, pady=10)

		# Boton Reporte Proyectos
		cargarArchivo = Button(self.tab2, text="Reporte Proyectos", command=self.ReporteProyectos, font=("Arial", 16, "bold"), bg="green", fg="white")
		cargarArchivo.grid(row=2, column=1, sticky="w", padx=10, pady=10)

		# Boton Reporte Tareas
		cargarArchivo = Button(self.tab2, text="Reporte Tareas", command=self.ReporteTareas, font=("Arial", 16, "bold"), bg="orange", fg="white")
		cargarArchivo.grid(row=2, column=2, sticky="w", padx=10, pady=10)

		self.treeview = Treeview(self.tab2, height=20, show='tree')

		# Configurar el widget Treeview
		self.treeview.grid(row=3, column=0, padx=10, pady=10, columnspan=3, sticky="nsew")

		self.ventana_empleado = Toplevel(self.ventana_login)
		self.ventana_empleado.title("Empleado")
		self.ventana_empleado.withdraw()

		# Crear un Frame para el Label y la imagen
		self.frame_empleado = Frame(self.ventana_empleado)
		self.frame_empleado.grid(row=0, column=0, sticky="w")

		# Crear un Label con el texto "Empleado"
		self.label_empleado = Label(self.frame_empleado, text="Empleado", font=("Arial", 20, "bold"))
		self.label_empleado.grid(row=0, column=0, sticky="e")

		# Cargar la imagen y redimensionarla
		absolutepath2 = os.path.abspath(__file__)
		Directorio2 = os.path.dirname(absolutepath)
		path2= Directorio2 + r'/img/empleado.png'
		self.imagen_empleado = PhotoImage(file=path2).subsample(5)

		# Crear un Label con la imagen
		self.imagen_label_empleado = Label(self.frame_empleado, image=self.imagen_empleado)
		self.imagen_label_empleado.grid(row=0, column=2, sticky="e")

		# Crear un botón
		self.SalirEmpleado = Button(self.frame_empleado, text="Cerrar Sesión", font=("Arial", 16, "bold"),bg="red", fg="white", command=self.CerrarSesionEmpleado)
		self.SalirEmpleado.grid(row=0, column=3, sticky="w")

		# Crear el widget Notebook
		self.notebook_empleado = Notebook(self.ventana_empleado)
		self.notebook_empleado.grid(row=1, column=0, sticky="nsew")

		# Crear la primera pestaña con una tabla
		self.tab1_empleado = Frame(self.notebook_empleado)
		self.notebook_empleado.add(self.tab1_empleado, text="Tareas")

		# Crear una lista con las opciones del Combobox
		opciones = ["Sin ningun Filtro", "Proyecto 1", "Proyecto 2", "Proyecto n"]

		# Función de acción para el Combobox
		def seleccionar_opcion(event):
			opcion = combobox_tareas_empleados.get()
			if opcion == "Sin ningun Filtro":
				tkinter.messagebox.showinfo("Opción seleccionada", "Ha seleccionado la opción 'Sin ningun Filtro'")
			elif opcion == "Proyecto 1":
				tkinter.messagebox.showinfo("Opción seleccionada", "Ha seleccionado la opción 'Proyecto 1'")
			elif opcion == "Proyecto 2":
				tkinter.messagebox.showinfo("Opción seleccionada", "Ha seleccionado la opción 'Proyecto 2'")
			elif opcion == "Proyecto n":
				tkinter.messagebox.showinfo("Opción seleccionada", "Ha seleccionado la opción 'Proyecto n'")

		# Crear el Combobox
		combobox_tareas_empleados = Combobox(self.tab1_empleado, values=opciones)
		combobox_tareas_empleados.insert(0, "Filtrar")
		combobox_tareas_empleados.grid(row=2, column=0, sticky="w",padx=10, pady=10)

		# Asociar la función de acción al Combobox
		combobox_tareas_empleados.bind("<<ComboboxSelected>>", seleccionar_opcion)

		# Crear la self.tablaEmpleados	
		self.tablaTareas = Treeview(self.tab1_empleado, columns=("Código de tarea","Nombre del proyecto","Nombre de la tarea"))
		self.tablaTareas.heading("Código de tarea", text="Código de tarea")
		self.tablaTareas.heading("Nombre del proyecto", text="Nombre del proyecto")
		self.tablaTareas.heading("Nombre de la tarea", text="Nombre de la tarea")
		self.tablaTareas["show"] = "headings"
		self.tablaTareas.grid(row=4, column=0, sticky="nsew", padx=10, pady=10, columnspan=2, rowspan=2)

		# Loop de modo grafico
		self.ventana_login.mainloop()
		
	def login(self):
		self.ventana_login.withdraw()
		self.ventana_admin.deiconify()

	def CerrarSesionAdmin(self):
		self.ventana_admin.withdraw()
		self.ventana_login.deiconify()
		self.usuario_entry.delete(0, END)
		self.contrasena_entry.delete(0, END)

	def loginEmpleado(self):
		self.ventana_login.withdraw()
		self.ventana_empleado.deiconify()
		
	def CerrarSesionEmpleado(self):
		self.ventana_empleado.withdraw()
		self.ventana_login.deiconify()
		self.usuario_entry.delete(0, END)
		self.contrasena_entry.delete(0, END)

	def admin(self):
		self.ventana_admin.withdraw()
		self.ventana_login.deiconify()

	def verificar_login(self):
		username = self.usuario_entry.get()
		password = self.contrasena_entry.get()

		if username == "PM-201907343" and password == "123":
			tkinter.messagebox.showinfo("Login Exitoso", "¡Bienvenido, PM-201907343!")
			return self.login()
		elif (len(ListaEmpleados)>0):
			for empleado in ListaEmpleados:
				if empleado[0] == username and empleado[2] == password:
					tkinter.messagebox.showinfo("Login Exitoso", "¡Bienvenido, "+empleado[1]+"!")
					return self.loginEmpleado()
			tkinter.messagebox.showerror("Error de Login", "Credenciales inválidas")
		else:
			tkinter.messagebox.showerror("Error de Login", "Credenciales inválidas")

	def calcular_hash(self,valores):
		# Concatenar los valores de entrada como una cadena
		cadena = ",".join(valores)
		
		# Calcular un hash simple basado en la suma de los valores ASCII de la cadena
		hash_valor = 0
		for caracter in cadena:
			hash_valor += ord(caracter)
		
		# Convertir el valor de hash en una cadena hexadecimal
		codigo_hash = binascii.hexlify(hash_valor.to_bytes((hash_valor.bit_length() + 7) // 8, byteorder='big')).decode()

		return codigo_hash

	def AgregarEmpleados(self):
		ruta_proyecto = os.getcwd()
		ruta_archivo = filedialog.askopenfilename(initialdir=ruta_proyecto, title="Seleccionar Empleados", filetypes=[('Archivo CSV', '*.csv')])
		empleados = []
		with open(ruta_archivo, "r") as f:
			next(f)  # Saltar la primera línea
			for linea in f:
				valores = linea.strip().split(",")
				codigo_hash = self.calcular_hash(valores)  # Calcular el código hash único
				valores.append(codigo_hash)  # Agregar el código hash a los valores
				empleado = [
					valores[0].strip(),
					valores[1].strip(),
					valores[2].strip(),
					valores[3].strip(),
					valores[4].strip()  # Agregar el código hash a la lista de empleados
				]
				empleados.append(empleado)

		# Verificar si los empleados ya existen y reemplazarlos si es necesario
		empleados_dict = {empleado[0]: empleado for empleado in empleados}
		for i, empleado in enumerate(ListaEmpleados):
			if empleado[0] in empleados_dict:
				ListaEmpleados[i] = empleados_dict[empleado[0]]
				del empleados_dict[empleado[0]]
		ListaEmpleados.extend(empleados_dict.values())

		# Mostrar los empleados en la tabla
		self.tablaEmpleados.delete(*self.tablaEmpleados.get_children())
		for empleado in ListaEmpleados:
			self.tablaEmpleados.insert("", "end", values=empleado)

	def cargar_json(self):
		contador=0
		# Abrir el cuadro de diálogo para seleccionar el archivo
		ruta_proyecto = os.getcwd()
		archivo = filedialog.askopenfilename(initialdir=ruta_proyecto, title="Seleccionar Proyectos",filetypes=[('Archivo JSON', '*.json')])

		# Leer el archivo JSON
		with open(archivo) as f:
			data = json.load(f)

		# Obtener la lista de proyectos
		proyectos = data['Proyectos']

		# Recorrer la lista de proyectos y agregar cada proyecto a la lista ListaTareas
		for proyecto in proyectos:
			id_proyecto = proyecto['id']
			nombre_proyecto = proyecto['nombre']
			prioridad_proyecto = proyecto['prioridad']
			tareas_proyecto = proyecto['tareas'] if proyecto['tareas'] is not None else []
			proyecto_dict = {
				'id': id_proyecto,
				'nombre': nombre_proyecto,
				'prioridad': prioridad_proyecto,
				'tareas': tareas_proyecto
			}
			ListaTareas.append(proyecto_dict)

			# Insertar los ítems en el árbol
			contador2 = 0
			nproyecto = str(id_proyecto) + " " + str(nombre_proyecto) + " " + str(prioridad_proyecto)
			self.treeview.insert("", "end", "i"+str(contador), text=nproyecto)
			if tareas_proyecto:
				for tarea in tareas_proyecto:
					contador2 += 1
					ntarea = str(tarea['nombre'])+ " " + str(tarea['empleado'])
					self.treeview.insert("i"+str(contador), "end", "i"+str(contador)+"."+str(contador2), text=ntarea)

			contador += 1


	def ReporteProyectos(self):
		
		global Tree
		Tree = AVLTree()
		global root
		root = None
	
		# Itera sobre cada diccionario en la lista
		for proyecto in ListaTareas:
			proyecto_id = proyecto['id']
			proyecto_nombre = proyecto['nombre']
			proyecto_prioridad = proyecto['prioridad']
			root = Tree.insert(root,str(proyecto_id), str(proyecto_nombre),str(proyecto_prioridad) )

		# Preorder Traversal
		print("Preorden de recorrido del árbol AVL construido es")
		Tree.preOrder(root)
		print()

		Tree.export_graphviz(root)

	def ReporteTareas(self):
		pass


if __name__ == "__main__":
	MyApp()
