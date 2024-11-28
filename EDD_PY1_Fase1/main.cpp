#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <string>

// Librerias de lista doble crear empleados
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
// Librerias de lista doble crear proyectos
#include "node.cpp"
#include "doubleList.cpp"
// Librerias para crear matriz dispersa
#include "matrix.cpp"

using namespace std;

//variables globales
SparseMatrix *matrix = new SparseMatrix();
int colDispersa=0, filaDispersa=0;
DoubleList *list = new DoubleList();
int cod_actual=100;
int id_actual=1;
struct Empleado {
    std::string id;
    std::string nombre;
    std::string contraseña;
    std::string puesto;
};
Empleado empleado;
std::vector<Empleado> empleados;
// Activacion de Funciones
void login();
void CEmpleados();
void CEmpleadosM();
void CEmpleadosMS();
void cargaArchivo();
string generar_IdEmpleado(string id);
void CProyecto();
void RCProyecto();
string generar_codigo();
void AProyecto();
string buscarEmpleadoPorNombre(string nombre);
void verificarEmpleado(string nombreBuscado);
void CTarea();
void RCEmpleados();
void ATarea();
void AReportes();
void RAReportes();

void login(){
    std::string usuario_correcto = "PM-201907343";
    std::string contrasena_correcta = "pmPassword123";
    
    std::string usuario_ingresado;
    std::string contrasena_ingresada;
    
    while (true) {
        cout<<"************       EDD ProyectUp      *************"<<endl;
        cout<<"Usuario: PM-201907343"<<endl;
        std::cin >> usuario_ingresado;
        
        cout<<"Password: pmPassword123"<<endl;
        std::cin >> contrasena_ingresada;
        
        if (usuario_ingresado == usuario_correcto && contrasena_ingresada == contrasena_correcta) {
            system("clear");
            std::cout << "Inicio de sesión exitoso. ¡Bienvenido!" << std::endl;
            break;
        } else {
            system("clear");
            std::cout << "Nombre de usuario o contraseña incorrectos. Inténtalo de nuevo." << std::endl;
        }
    }
}

void menu(){
    int menu=0;
    //Menu de ProyectUp
    while (true)
    {
        cout<<"************       EDD ProyectUp      ************"<<endl;
        cout<<"************  Bienvenido PM-201907343 ************"<<endl;
        cout<<"1. Cargar empleados"<<endl;
        cout<<"2. Carga proyecto"<<endl;
        cout<<"3. Asignar Proyecto"<<endl;
        cout<<"4. Crear tareas "<<endl;
        cout<<"5. Asignar tareas"<<endl;
        cout<<"6. Area de reportes"<<endl;
        cout<<"7. Salir"<<endl;
        cout<<"Elije una opcion: "<<endl;
        cin>>menu;
        system("clear");
        switch (menu)
        {
            case 1:
                CEmpleados();
                break;
            case 2:
                CProyecto();
                break;
            case 3:
                AProyecto();
                break;
            case 4:
                CTarea();
                break;
            case 5:
                ATarea();
                break;
            case 6:
                AReportes();
                break;;
            case 7:
                system("clear");
                cout<<"Has salido del sistema exitos en todo";
                // Terminar el programa con exit code 0 (éxito)
                exit(0);
                break;
            default:
                cout<<"Haz ingresado un caracter no valido vuelve a intentarlo"<<endl;
                break;
        }
    }
    
    
}

void CEmpleados(){
    //Cargar Empleados
    int opcion;
    cout<<"************       EDD ProyectUp      ************"<<endl;
    cout<<"************  Bienvenido PM-201907343 ************"<<endl;
    cout<<"************    Menu Carga Empleados  ************"<<endl;    
    cout<<"1. Cargar Manual"<<endl;
    cout<<"2. Carga Masiva"<<endl;
    cout<<"Elije una opcion: "<<endl;
    cin>>opcion;
    system("clear");
    switch (opcion)
    {
        case 1:
            CEmpleadosM();
            break;
        case 2:
            CEmpleadosMS();
            break;
        default:
            cout<<"Haz ingresado un caracter no valido vuelve a intentarlo"<<endl;
            RCEmpleados();
            break;
    }
}

void CEmpleadosM(){
//cargar manual empleados
    string name;
    string password;
    int op;
    string codigoCManual;
    string tipoEmpleado;
    string opSalir;
    printf("************       EDD ProyectUp      ************\n");
    printf("************  Bienvenido PM-201907343 ************\n");
    printf("************Carga de Empleados Manual ************\n");
    
    //Añadir ingreso de nombre y contraseña de forma manual
    printf("Nombre:\n");
    cin>>name;
    printf("Contraseña:\n");
    cin>>password;
    printf("Puestos disponibles:\n");
    printf("1. Developer Frontend\n");
    printf("2. Developer Backend\n");
    printf("3. Quality Assurance\n");
    printf("Elija una opción:\n");
    cin>>op;
    system("clear");
    if (op == 1) {
        tipoEmpleado = "Developer Frontend";
        codigoCManual = generar_IdEmpleado("FDEV-");
        printf("Agregado exitosamente, Id generado: %s\n", codigoCManual.c_str());
        empleado.id = codigoCManual;
        empleado.nombre = name;
        empleado.contraseña = password;
        empleado.puesto = tipoEmpleado;
        empleados.push_back(empleado);
        RCEmpleados();
    } else if (op == 2) {
        tipoEmpleado = "Developer Backend";
        codigoCManual = generar_IdEmpleado("BDEV-");
        printf("Agregado exitosamente, Id generado: %s\n",codigoCManual.c_str());
        empleado.id = codigoCManual;
        empleado.nombre = name;
        empleado.contraseña = password;
        empleado.puesto = tipoEmpleado;
        empleados.push_back(empleado);
        RCEmpleados();
    } else if (op == 3) {
        tipoEmpleado = "Quality Assurance";
        codigoCManual = generar_IdEmpleado("QA-");
        printf("Agregado exitosamente, Id generado: %s\n",codigoCManual.c_str());
        empleado.id = codigoCManual;
        empleado.nombre = name;
        empleado.contraseña = password;
        empleado.puesto = tipoEmpleado;
        empleados.push_back(empleado);
        RCEmpleados();
    } else {
        printf("se cometio un error en el ingreso de los puestos disponibles\n");
        RCEmpleados();
    }
    
}

string generar_IdEmpleado(string id){
    string codigo="";
    if (id_actual<10)
    {
        codigo = id +"00"+ to_string(id_actual);
        id_actual++;
    }else if (id_actual<100)
    {
        codigo = id +"0"+ to_string(id_actual);
        id_actual++;
    }else if (id_actual<100)
    {
        codigo = id + to_string(id_actual);
        id_actual++;
    }else{
        printf("Ya no existen mas codigos disponibles para ingresos");
        menu();
    }
    
    
    return codigo;
}

void CEmpleadosMS(){
    //Carga masiva empleados
    printf("************       EDD ProyectUp      ************\n");
    printf("************  Bienvenido PM-201907343 ************\n");
    printf("************Carga de Empleados Masiva ************\n");
    system("clear");
    cargaArchivo();
    RCEmpleados();
    
    //crear una opcion para repetir la carga masiva
    //Realizar un if para verificar si el archivo fue cargado o no en el sistema
    //Mandar los datos cargados en memoria a una lista enlazada y posteriormente regresar al menu de cargas
}

void cargaArchivo(){
    std::string nombreArchivo;
    printf("Ingrese el nombre del archivo con la extensión .csv: ");
    std::cin >> nombreArchivo;

    std::ifstream archivo(nombreArchivo);
    
    if (!archivo.is_open()) {
        printf("Error al abrir el archivo.\n");
        menu();
    }

    std::string linea;

    // Omitir la línea de encabezado
    std::getline(archivo, linea);
    
    

    while (std::getline(archivo, linea)) {
        std::istringstream iss(linea);
        std::string id, nombre, contraseña, puesto;

        std::getline(iss, id, ',');
        std::getline(iss, nombre, ',');
        std::getline(iss, contraseña, ',');
        std::getline(iss, puesto);

        
        empleado.id = id;
        empleado.nombre = nombre;
        empleado.contraseña = contraseña;
        empleado.puesto = puesto;

        empleados.push_back(empleado);
    }

    // Imprimir los datos capturados
    for (const auto& empleado : empleados) {
        printf("ID: %s\n", empleado.id.c_str());
        printf("Nombre: %s\n", empleado.nombre.c_str());
        printf("Contraseña: %s\n", empleado.contraseña.c_str());
        printf("Puesto: %s\n", empleado.puesto.c_str());
        printf("\n");
    }

    printf("Carga Exitosa...\n");
}

void RCEmpleados(){
    char repetir;
    cout<<"Desea volver a repetir la carga de empleados escriba S/N";
    cin>>repetir;
    repetir = toupper(repetir);
    switch (repetir)
    {
        case 'S':
            CEmpleados();
            break;
        case 'N':
            menu();
            break;
        default:
            cout<<"Ingresaste un caracter no valido intentalo de nuevo";
            RCEmpleados();
            break;
    }     
}

void CProyecto(){
    //Crear Proyecto
    string Nproyecto = "";
    string tipo = "";
    string codigo = generar_codigo();

    cout<<"************       EDD ProyectUp      ************"<<endl;
    cout<<"************  Bienvenido PM-201907343 ************"<<endl;
    cout<<"************      Menu de proyecto    ************"<<endl;
    cout<<"Nombre de proyecto:"<<endl;
    cin>>Nproyecto;
    // validar que la prioridad solo puede ser del tipo A,B,C
    cout<<"Tipo de Prioridad: "<<endl;
    cin>>tipo;
    system("clear"); 
    if (tipo == "A") {
        list->add(Nproyecto,tipo,codigo);
        std::cout << "Tipo de prioridad A" << std::endl;
        RCProyecto();
    } else if (tipo == "B") {
        list->add(Nproyecto,tipo,codigo);

        std::cout << "Tipo de prioridad B" << std::endl;
        RCProyecto();
    } else if (tipo == "C") {
        list->add(Nproyecto,tipo,codigo);
        std::cout << "Tipo de prioridad C" << std::endl;
        RCProyecto();
    } else {
        std::cout << "La prioridad que ingresaste no es válida,\nVerifica que sea (A, B o C)" << std::endl;
        RCProyecto();
    }

    // verificar que se creo el nuevo proyecto, mostrar un mensaje si sale un error y volver al menu de proyecto
    // por ultimo se deve de mostrar una opcion para salir del menu proyecto y regresar al menu principal
    cout<<"Creado exitosamente, PY-103"<<endl;
}

void RCProyecto(){
    char repetir;
    cout<<"Desea volver a repetir la carga de un proyecto escriba S/N";
    cin>>repetir;
    system("clear");
    repetir = toupper(repetir);
    switch (repetir)
    {
        case 'S':
            CProyecto();
            break;
        case 'N':
            menu();
            break;
        default:
            cout<<"Ingresaste un caracter no valido intentalo de nuevo";
            RCProyecto();
            break;
    }  
}

string generar_codigo(){
    std::string codigo = "PY-" + std::to_string(cod_actual);
    cod_actual++;
    if (cod_actual > 999)
    {
        printf("Ya no puedes agregar mas codigos\n");
    }
    return codigo;  
}

void AProyecto(){
   string name,codP;
    //Crear Tarea
    cout<<"************       EDD ProyectUp      ************"<<endl;
    cout<<"************  Bienvenido PM-201907343 ************"<<endl;
    cout<<"********* Menu de Asignacion de proyecto ************"<<endl;
    cout<<"Escribe el nombre de un empleado:"<<endl;
    cin>>name;
    verificarEmpleado(name);
    cout<<"Escribe el codigo del proyecto:"<<endl;
    cin>>codP;
    if (list->verificarNpy(codP) == true)
    {
        system("clear");
        // agregar a la matriz dispersa
        
        //matrix->createNode(Nfila, Ncol, NombreFila,NombreColumna,Compbinacion Cod desarrollador + cod Proyecto);
        
        matrix->createNode(colDispersa, filaDispersa, name,"Tipo", codP);
        printf("Asignacion de proyecto se realizo de forma correcta\n");
        menu();
        
    }else{
        system("clear");
        cout<<"No se encontro ningun proyecto con ese nombre"<<endl;
        menu();
    }

     
}

string buscarEmpleadoPorNombre(string nombre) {
    for (const Empleado& empleado : empleados) {
        if (empleado.nombre == nombre) {
            return empleado.id;
        }
    }
    return ""; // Si no se encuentra ningún empleado con ese nombre, se devuelve una cadena vacía
}

void verificarEmpleado(string nombreBuscado){
    bool empleadoExiste = false;

    for (const auto& empleado : empleados) {
        if (empleado.nombre == nombreBuscado) {
            empleadoExiste = true;
            break;
        }
    }

    if (empleadoExiste) {
        cout << "El empleado con el nombre \"" << nombreBuscado << "\" existe en la lista de empleados." << std::endl;
    } else {
        cout << "El empleado con el nombre \"" << nombreBuscado << "\" no existe en la lista de empleados." << std::endl;
        menu();
    }
}

void CTarea(){
    string Tareas,NomTarea;
    //Crear Tarea
    cout<<"************       EDD ProyectUp      ************"<<endl;
    cout<<"************  Bienvenido PM-201907343 ************"<<endl;
    cout<<"************       Menu de Tareas     ************"<<endl;
    cout<<"PY-100. Sistema de inventario Vestidos Julieta"<<endl;   
    cout<<"PY-101. Tienda Online Restaurante Giovanni"<<endl;
    cout<<"PY-102. Sistema de inventario EPA"<<endl;
    cout<<"PY-103. Sistema de inventario Shadai"<<endl;
    cout<<"Elije un proyecto:"<<endl;
    cin>>Tareas;
    cout<<"Nombre de la tarea:"<<endl;
    cin>>NomTarea;
    system("clear");
    cout<<"Tarea ingresada correctamente"<<endl;
    menu();
}

void ATarea(){
    cout<<"************       EDD ProyectUp      ************"<<endl;
    cout<<"************  Bienvenido PM-201907343 ************"<<endl;
    cout<<"************   Menu de Asignar Tareas ************"<<endl;

}

void AReportes(){
    string valor ="hola";
    int op;
    cout<<"************       EDD ProyectUp      ************"<<endl;
    cout<<"************  Bienvenido PM-201907343 ************"<<endl;
    cout<<"************      Areas de Reportes   ************"<<endl;
    cout<<"1. Reporte de Matriz Dispersa"<<endl;
    cout<<"2. Reporte de la cola"<<endl;
    cout<<"3. Reporte JSON"<<endl;
    cout<<"4. Regresar"<<endl;
    cin>>op;
    system("clear");
    switch (op)
    {
    case 1:
        cout<<"Reporte de Matriz dispersa Creado Correctamente"<<endl;
        matrix->getGraphviz();
        break;
    case 2:
        list->generateGraphvizFile("Grafico_Cola");
        cout<<"Grafico de la cola creado correctamente"<<endl;
        break;
    case 3:
        cout<<"Funcion JSON aun no creada"<<endl;
        break;
    case 4:
        menu();
        break;
    default:
        cout<<"El dato que ingresaste no corresponde con la lista"<<endl;
        AReportes();
        break;
    }
}


void RAReportes(){
    char repetir;
    cout<<"Desea volver a ver un reporte escriba S/N";
    cin>>repetir;
    system("clear");
    repetir = toupper(repetir);
    switch (repetir)
    {
        case 'S':
            AReportes();
            break;
        case 'N':
            menu();
            break;
        default:
            cout<<"Ingresaste un caracter no valido intentalo de nuevo";
            RAReportes();
            break;
    }  
}

int main(){
    //Login de app
        
    // Activar funcion de login cuando ya no existan datos quemados
    //login();

    menu();
    
    cout<<""<<endl;
return 0;
}