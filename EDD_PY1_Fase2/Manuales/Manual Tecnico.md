# <font color="blue">📚 Manual Técnico: Sistema de Gestión de Empleados y Proyectos</font>

## <font color="green">📋 Índice</font>
1. [🏁 Introducción](#introducción)
2. [📚 Bibliotecas Importadas](#bibliotecas-importadas)
3. [🖥️ Clase `MyApp`](#clase-myapp)
   - [🔧 Método `__init__(self)`](#método-initself)
   - [🔑 Método `login(self)`](#método-loginself)
   - [🚪 Método `CerrarSesionAdmin(self)`](#método-cerrarsesionadminself)
   - [🔑 Método `loginEmpleado(self)`](#método-loginempleadoself)
   - [🚪 Método `CerrarSesionEmpleado(self)`](#método-cerrarsesionempleadoself)
   - [🚀 Método `admin(self)`](#método-adminself)
   - [🔍 Método `verificar_login(self)`](#método-verificar_logins)
   - [➕ Método `AgregarEmpleados(self)`](#método-agregarempleadoss)
   - [📂 Método `cargar_json(self)`](#método-cargar_jsonself)
   - [🔍 Método `seleccionar_opcion(self)`](#método-seleccionar_opcions)
4. [🔚 Conclusión](#conclusión)

## <font color="green">🏁 Introducción</font>
Este manual técnico proporciona una descripción detallada del Sistema de Gestión de Empleados y Proyectos implementado en Python utilizando la biblioteca Tkinter y la manipulación de archivos JSON. El sistema permite la gestión de empleados, proyectos y tareas asociadas.

## <font color="green">📚 Bibliotecas Importadas</font>
El código utiliza varias bibliotecas que son fundamentales para su funcionamiento. Aquí están las bibliotecas importadas y su propósito:

- `<font color="red">🖼️ tkinter</font>`: Utilizada para crear la interfaz gráfica de usuario.
- `<font color="red">💾 filedialog</font>`: Proporciona cuadros de diálogo para seleccionar archivos.
- `<font color="red">💬 tkinter.messagebox</font>`: Utilizada para mostrar mensajes y alertas.
- `<font color="red">🖥️ os</font>`: Proporciona funciones para interactuar con el sistema operativo, como obtener rutas de archivos y directorios.
- `<font color="red">📟 tkinter.ttk</font>`: Proporciona widgets de interfaz gráfica de usuario más avanzados.
- `<font color="red">🌐 webbrowser</font>`: Utilizada para abrir enlaces web en el navegador.

## <font color="green">🖥️ Clase `MyApp`</font>
La clase `MyApp` es la clase principal que inicia la aplicación. Aquí se encuentran los elementos principales de la interfaz de usuario y las funciones que manejan eventos específicos.

### <font color="blue">🔧 Método `__init__(self)`</font>
- Este método es el constructor de la clase y se ejecuta cuando se crea una instancia de la clase.
- Crea la ventana principal de inicio de sesión.
- Define varios widgets, como cuadros de texto, etiquetas y botones, en la ventana de inicio de sesión.
- Configura la ventana principal para mostrar un icono personalizado.
- Crea una segunda ventana (`self.ventana_admin`) para la interfaz de administrador pero la mantiene oculta.
- Crea una tercera ventana (`self.ventana_empleado`) para la interfaz de empleado pero la mantiene oculta.
- Inicializa un widget `Notebook` que permite alternar entre pestañas de Empleados y Proyectos/Tareas.
- Define botones para cargar archivos CSV y JSON, así como para generar informes.
- Configura una tabla (`self.tablaEmpleados`) para mostrar información de empleados.
- Asocia eventos y funciones a los widgets, como `command=self.verificar_login` para el botón de inicio de sesión.
- Ejecuta el bucle principal de la interfaz gráfica con `self.ventana_login.mainloop()`.

```python
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
        usuariolabel = Label(self.ventana_login, text="Usuario:")
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

        # ... (código restante)

        # Loop de modo grafico
        self.ventana_login.mainloop()
```

### <font color="blue">🔑 Método `login(self)`</font>
- Oculta la ventana de inicio de sesión y muestra la ventana de administrador.

```python
def login(self):
    self.ventana_login.withdraw()
    self.ventana_admin.deiconify()
```


### <font color="blue">🚪 Método `CerrarSesionAdmin(self)`</font>
- Oculta la ventana de administrador y muestra la ventana de inicio de sesión.
- Borra los campos de usuario y contraseña.

```python
def CerrarSesionAdmin(self):
    self.ventana_admin.withdraw()
    self.ventana_login.deiconify()
    self.usuario_entry.delete(0, END)
    self.contrasena_entry.delete(0, END)
```

### <font color="blue">🔑 Método `loginEmpleado(self)`</font>
- Oculta la ventana de inicio de sesión y muestra la ventana de empleado.

```python
    def loginEmpleado(self):
        self.ventana_login.withdraw()
        self.ventana_empleado.deiconify()

```

### <font color="blue">🚪 Método `CerrarSesionEmpleado(self)`</font>
- Oculta la ventana de empleado y muestra la ventana de inicio de sesión.
- Borra los campos de usuario y contraseña.

```python
    def CerrarSesionEmpleado(self):
        self.ventana_empleado.withdraw()
        self.ventana_login.deiconify()
        self.usuario_entry.delete(0, END)
        self.contrasena_entry.delete(0, END)
```

### <font color="blue">🚀 Método `admin(self)`</font>
- Oculta la ventana de administrador y muestra la ventana de inicio de sesión.

```python
    def admin(self):
        self.ventana_admin.withdraw()
        self.ventana_login.deiconify()
```

### <font color="blue">🔍 Método `verificar_login(self)`</font>
- Obtiene el nombre de usuario y la contraseña ingresados por el usuario.
- Verifica si las credenciales son válidas. Si son válidas, muestra la ventana de administrador o empleado según corresponda. Si no son válidas, muestra un mensaje de error.

```python
    def verificar_login(self):
        username = self.usuario_entry.get()
        password = self.contrasena_entry.get()

        if username == "PM-201907343" and password == "123":
            tkinter.messagebox.showinfo("Login Exitoso", "¡Bienvenido, PM-201907343!")
            return self.login()
        elif (len(ListaEmpleados) > 0):
            for empleado in ListaEmpleados:
                if empleado[0] == username and empleado[2] == password:
                    tkinter.messagebox.showinfo("Login Exitoso", "¡Bienvenido, "+empleado[1]+"!")
                    return self.loginEmpleado()
            tkinter.messagebox.showerror("Error de Login", "Credenciales inválidas")
        else:
            tkinter.messagebox.showerror("Error de Login", "Credenciales inválidas")
```

### <font color="blue">➕ Método `AgregarEmpleados(self)`</font>
- Abre un cuadro de diálogo para seleccionar un archivo CSV.
- Lee los datos del archivo CSV y agrega los empleados a la lista global `ListaEmpleados`.
- Muestra los empleados en la tabla de empleados en la pestaña correspondiente.

```python
    def AgregarEmpleados(self):
        ruta_proyecto = os.getcwd()
        ruta_archivo = filedialog.askopenfilename(initialdir=ruta_proyecto, title="Seleccionar archivo")
        empleados = []
        with open(ruta_archivo, "r") as f:
            next(f)  # Saltar la primera línea
            for linea in f:
                valores = linea.strip().split(",")
                empleado = [
                    valores[0].strip(),
                    valores[1].strip(),
                    valores[2].strip(),
                    valores[3].strip()
                ]
                empleados.append(empleado)

        # Agregar los empleados cargados a la lista global
        ListaEmpleados.extend(empleados)

        # Mostrar los empleados en la tabla
        for empleado in empleados:
            self.tablaEmpleados.insert("", "end", values=empleado)
```
### <font color="blue">📂 Método `cargar_json(self)`</font>
- Abre un cuadro de diálogo para seleccionar un archivo JSON.
- Lee los datos del archivo JSON y muestra información sobre proyectos y tareas en la pestaña correspondiente.
- Utiliza un widget `Treeview` para mostrar los datos de manera jerárquica.

```python
    def cargar_json(self):
        # Abrir el cuadro de diálogo para seleccionar el archivo
        archivo = filedialog.askopenfilename(filetypes=[('Archivo JSON', '*.json')])

        # Leer el archivo JSON
        with open(archivo) as f:
            data = json.load(f)

        # Obtener la lista de proyectos
        proyectos = data['Proyectos']

        contador = 0
        # Recorrer la lista de proyectos y mostrar la información
        for proyecto in proyectos:
            contador2 = 0
            nproyecto = str(proyecto['id']) + " " + str(proyecto['nombre']) + " " + str(proyecto['prioridad'])
            # Insertar los ítems en el árbol
            self.treeview.insert("", "end", "i"+str(contador), text=nproyecto)
            if(proyecto['tareas'] != None):
                for tarea in proyecto['tareas']:
                    contador2 += 1
                    ntarea = str(tarea['nombre'])+ " " + str(tarea['empleado'])
                    self.treeview.insert("i"+str(contador), "end", "i"+str(contador)+"."+str(contador2), text=ntarea)

            contador += 1

        ListaTareas = data
```

### <font color="blue">🔍 Método `seleccionar_opcion(self)`</font>
- Maneja la selección de opciones en el Combobox en la pestaña de tareas de empleado.
- Muestra un mensaje de información con la opción seleccionada.

```python
    def seleccionar_opcion(self):
        opcion = self.combobox_tareas_empleados.get()
        if opcion == "Sin ningun Filtro":
            tkinter.messagebox.showinfo("Opción seleccionada", "Ha seleccionado la opción 'Sin ningun Filtro'")
        elif opcion == "Proyecto 1":
            tkinter.messagebox.showinfo("Opción seleccionada", "Ha seleccionado la opción 'Proyecto 1'")
        elif opcion == "Proyecto 2":
            tkinter.messagebox.showinfo("Opción seleccionada", "Ha seleccionado la opción 'Proyecto 2'")
        elif opcion == "Proyecto n":
            tkinter.messagebox.showinfo("Opción seleccionada", "
```

## <font color="green">🔚 Conclusión</font>
Este manual técnico proporciona una descripción detallada del sistema de gestión de empleados y proyectos implementado en Python con la biblioteca Tkinter. El sistema permite a los usuarios iniciar sesión como administrador o empleado, cargar datos de empleados desde archivos CSV, y cargar y visualizar datos de proyectos y tareas desde archivos JSON.

<font color="purple">¡Gracias por utilizar nuestro sistema!</font>


# <span style="color:#2E7D32">🌳 Manual Técnico: Árbol AVL con Visualización Gráfica 📊</span>

---

# <span style="color:#1976D2">📚 Índice de Títulos</span>

- [Introducción](#introducción)
- [Estructura del Código](#estructura-del-código)
  - [`treeNode` Clase](#1-treenode-clase)
  - [`AVLTree` Clase](#2-avltree-clase)
  - [Visualización Gráfica](#3-visualización-gráfica)
- [Uso del Árbol AVL](#uso-del-árbol-avl)
- [Ejecución del Código](#ejecución-del-código)
- [Conclusión](#conclusión)

## <span style="color:#2E7D32">🚀 Introducción</span>
Este código implementa un Árbol AVL (Árbol de Búsqueda Binaria Balanceado por Altura) en Python. Un Árbol AVL es una estructura de datos de tipo árbol que se utiliza para almacenar elementos de manera ordenada y garantizar que el árbol se mantenga equilibrado, lo que asegura un tiempo de búsqueda eficiente.


## <span style="color:#1976D2">📦 Estructura del Código</span>
El código se divide en tres partes principales: la definición de la clase `treeNode`, la definición de la clase `AVLTree`, y la creación de un árbol AVL y su visualización.

### <span style="color:#1976D2">1. `treeNode` Clase</span>
- La clase `treeNode` representa los nodos individuales del árbol.
- Cada nodo tiene un valor numérico calculado a partir de su nombre, un nombre, y referencias a los nodos izquierdo (`l`) y derecho (`r`).
- La altura del nodo (`h`) se utiliza para mantener el equilibrio del árbol.

```python
class treeNode(object):
    def __init__(self, name):
        value = 0
        for character in name:
            value += ord(character)
        self.value = value
        self.name = name
        self.l = None
        self.r = None
        self.h = 1
```

### <span style="color:#1976D2">2. `AVLTree` Clase</span>
- La clase `AVLTree` contiene métodos para realizar operaciones en el árbol AVL, como inserción y rotaciones.
- Se calcula la altura (`h`) y el factor de balance (`b`) de un nodo para asegurar que el árbol esté balanceado.
- Los métodos `lRotate` y `rRotate` realizan rotaciones izquierda y derecha respectivamente para mantener el equilibrio.
- `insert` se utiliza para insertar un nuevo nodo en el árbol AVL.

```python
class treeNode(object):
    def __init__(self, name):
        value = 0
        for character in name:
            value += ord(character)
        self.value = value
        self.name = name
        self.l = None
        self.r = None
        self.h = 1
```

### <span style="color:#1976D2">3. Visualización Gráfica</span>
- El método `export_graphviz` genera un archivo DOT que representa el árbol AVL en formato Graphviz.
- El método `aux_export_graphviz` es una función auxiliar que ayuda a construir la representación DOT del árbol.
- Se utiliza Graphviz para generar una imagen PNG (`avlTree.png`) a partir del archivo DOT creado.

```python
def export_graphviz(self, root):
    dotContent = "digraph G {\n"
    auxContent = self.aux_export_graphviz(root) if root else ""
    if auxContent:
        dotContent += auxContent
    dotContent += "}"
    f = open("avlTree.dot", "w")
    f.write(dotContent)
    f.close()
    os.system(cmd)
```

## <span style="color:#1976D2">⚙️ Uso del Árbol AVL</span>
El código crea una instancia de `AVLTree` y realiza una serie de inserciones en el árbol. Luego, se imprime el recorrido en preorden del árbol.

```python
Tree = AVLTree()
root = None

root = Tree.insert(root, "hola")
root = Tree.insert(root, "adios amor")
root = Tree.insert(root, "casa")
root = Tree.insert(root, "perro")
root = Tree.insert(root, "gato")
root = Tree.insert(root, "casa1")
root = Tree.insert(root, "casa2")
root = Tree.insert(root, "casa3")
root = Tree.insert(root, "casa1")
```

## <span style="color:#1976D2">🎉 Ejecución del Código</span>
Para ejecutar el código, se deben seguir los siguientes pasos:

1. Asegúrate de tener instalado Graphviz en tu sistema, ya que se utiliza para generar la representación gráfica del árbol.

2. Ejecuta el código Python en un entorno que admita la librería `os`.

3. El método `Tree.export_graphviz(root)` generará un archivo `avlTree.dot` y luego ejecutará Graphviz para crear `avlTree.png`.

4. Se imprimirá el recorrido en preorden del árbol en la consola.

## <span style="color:#2E7D32">🔍 Conclusión</span>
El código proporcionado implementa un Árbol AVL y ofrece una forma de visualizarlo. Esta estructura de datos es útil en aplicaciones que requieren una búsqueda eficiente de datos ordenados.
