 # EDD_PY1_Fase1


### Objetivo general:

● Aplicar los conocimientos del curso Estructuras de Datos en el desarrollo de
las diferentes estructuras de datos y los diferentes algoritmos de
manipulación de la información en ellas.

### Objetivos específicos:

● Utilizar el lenguaje C++ para implementar estructuras de datos lineales

● Utilizar la herramienta Graphviz para graficar las estructuras de datos.

● Definir e implementar algoritmos de búsqueda e inserción para las listas
enlazadas, matrices dispersas y colas.


## Caracteristicas

* Crear y gestionar proyectos
* Crear y asignar tareas
* Gestionar empleados
* Generar informes

## Instalación

Para instalar EDD_PY1_Fase1, clona el repositorio y ejecuta los siguientes comandos:

```
git clone git@gitlab.com:BrayanMica/edd_2s2023_py_201907343.git
npm install
```

## Uso

Para usar el proyecto primero descargalo y posteriormente en la carpeta raiz ejecuta:

En una ventana de comandos de (Linux) ejecuta la siguiente linea de comandos: 
* g++ main.cpp doubleList.cpp node.cpp -o main && ./main:

O bien en un IDE como Visual Studio Code o Eclipse para Linux.


# Manual de Tecnico - EDD_PY1

Este manual te guiará a través del uso del programa **EDD ProyectUp**. El programa es una herramienta de gestión de proyectos y tareas. A continuación, se describen las principales funcionalidades y cómo utilizarlas.

## 📋 Contenido
1. [Requisitos](#requisitos)
2. [Inicio de Sesión](#inicio-de-sesion)
3. [Menú Principal](#menu-principal)
4. [Carga de Empleados](#carga-de-empleados)
5. [Creación de Proyectos](#creacion-de-proyectos)
6. [Creación de Tareas](#creacion-de-tareas)
7. [Asignación de Tareas](#asignacion-de-tareas)
8. [Área de Reportes](#area-de-reportes)
9. [Salir](#salir)

## 📌 Requisitos <a name="requisitos"></a>

Antes de comenzar, asegúrate de tener instalado un entorno de desarrollo que admita C++ y las bibliotecas necesarias para compilar y ejecutar el código.

## 🔐 Inicio de Sesión <a name="inicio-de-sesion"></a>

El programa **EDD ProyectUp** requiere un inicio de sesión. Las credenciales predeterminadas son las siguientes:
- Usuario: **PM-201907343**
- Contraseña: **pmPassword123**

```cpp
// Ejemplo de inicio de sesión en C++
while (true) {
    // Código de inicio de sesión
    if (usuario_ingresado == usuario_correcto && contrasena_ingresada == contrasena_correcta) {
        // Inicio de sesión exitoso
        break;
    } else {
        // Inicio de sesión fallido
    }
}
```

Una vez que hayas ingresado las credenciales correctas, podrás acceder al **menú principal**.

## 🏁 Menú Principal <a name="menu-principal"></a>

El menú principal te permite acceder a las siguientes funcionalidades:
1. **Cargar Empleados**: Permite cargar empleados manualmente o de forma masiva.
2. **Cargar Proyecto**: Permite crear un nuevo proyecto.
3. **Crear Tareas**: Permite crear tareas para un proyecto existente.

```cpp
// Ejemplo de creación de tareas en C++
string proyecto_seleccionado;
string nombre_tarea;
```

4. **Asignar Tareas**: Asigna tareas a empleados.

```cpp
// Ejemplo de asignación de tareas en C++
string proyecto_seleccionado;
string tarea_seleccionada;
string empleado_asignado;
```

5. **Área de Reportes**: Genera informes relacionados con el proyecto y las tareas.
6. **Salir**: Cierra la aplicación.

## 📂 Carga de Empleados <a name="carga-de-empleados"></a>

La carga de empleados te permite agregar nuevos empleados al sistema. Puedes elegir entre dos opciones:
1. **Cargar Manual**: Agrega empleados ingresando su nombre, contraseña y puesto.
2. **Carga Masiva**: Permite cargar empleados desde un archivo CSV llamado "calificacion.csv".

## 🚀 Creación de Proyectos <a name="creacion-de-proyectos"></a>

Puedes crear proyectos dentro del sistema. Para crear un proyecto, sigue estos pasos:
1. Ingresa el nombre del proyecto.
2. Especifica el tipo de prioridad (A, B o C).

El programa generará automáticamente un código de proyecto único.

## ✏️ Creación de Tareas <a name="creacion-de-tareas"></a>

La creación de tareas te permite agregar tareas a proyectos existentes. Selecciona el proyecto al que deseas agregar una tarea y proporciona el nombre de la tarea.

## 📝 Asignación de Tareas <a name="asignacion-de-tareas"></a>

Esta función te permite asignar tareas a empleados. Selecciona el proyecto y la tarea que deseas asignar a un empleado.

## 📊 Área de Reportes <a name="area-de-reportes"></a>

En esta sección, puedes generar diferentes tipos de informes relacionados con el proyecto y las tareas. Las opciones disponibles son:
1. **Reporte de Matriz Dispersa**: Genera un informe de la matriz dispersa.
2. **Reporte de la Cola**: Crea un gráfico de la cola de tareas.
3. **Reporte JSON**: Esta función aún no está implementada.

## 🚪 Salir <a name="salir"></a>

La opción "Salir" cierra la aplicación **EDD ProyectUp**.

¡Disfruta de la gestión de proyectos y tareas con **EDD ProyectUp**!

---

*Nota: Este manual se proporciona con fines informativos. Los detalles específicos pueden variar según la implementación y la versión del programa.*

  # 💪 Implementacion de Matriz dispersa en C++ con visualización de Graphviz

## Introducción
Una matriz dispersa es una matriz en la cual la mayoría de los elementos son cero. Las matrices dispersas se utilizan con frecuencia para representar datos del mundo real que son dispersos por naturaleza, como gráficos, imágenes y datos científicos.

## Implementación
El código para una matriz dispersa en C++ se proporciona a continuación. La implementación utiliza una lista enlazada para almacenar los elementos no nulos de la matriz. Cada nodo en la lista enlazada representa un elemento no nulo y contiene los índices de fila y columna del elemento, así como el valor del elemento.


```c++
#include <stdio.h>
#include <stdlib.h>
#include "matrix.h"
#include "nodeDispersa.h"
#include <string>

using namespace std;
```

```c++
// get string if value is -1
string getVal(int val)
{
    if (val == -1)
    {
        return "head";
    }
    return to_string(val);
}
```
```c++
// constructor
SparseMatrix::SparseMatrix()
{
    head = new Node;
    head->row = -1;
    head->col = -1;
    head->val = -1;
    // conexiones de nodo
    head->up = NULL;
    head->down = NULL;
    head->left = NULL;
    head->right = NULL;
}
```

```c++
// create node
Node *SparseMatrix::createNode(int row, int col, int val)
{
    Node *newNode = new Node;
    newNode->row = row;
    newNode->col = col;
    newNode->val = val;
    newNode->up = NULL;
    newNode->down = NULL;
    newNode->left = NULL;
    newNode->right = NULL;

    // Apuntan a las cabeceras veritcal y horizontal 
    Node *temp = createVertHead(row);
    Node *temp2 = createHorzHead(col);

    // Apuntan a la derecha y abajo del nodo actual
    Node *temp3 = temp->right;
    Node *temp4 = temp2->down;

    // Busqueda horizontal e insercion
    while (temp3 != NULL)
    {
        if (temp3->col > col)
```
## Contribuciones

Damos la bienvenida a las contribuciones a EDD_PY1_Fase1. Si encuentras un error, por favor presenta un problema. Si tienes una solicitud de función, por favor crea una solicitud de extracción.

## Licencia

EDD_PY1_Fase1 está bajo la licencia Brayan Estiben Micá Pérez.


### ©️ dllnebles@gmail.com👍

