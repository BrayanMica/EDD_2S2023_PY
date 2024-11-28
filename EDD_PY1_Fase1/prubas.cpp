#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

struct Empleado {
    std::string id;
    std::string nombre;
    std::string contraseña;
    std::string puesto;
};

int main() {
    std::string nombreArchivo;
    std::cout << "Ingrese el nombre del archivo con la extensión .csv: ";
    std::cin >> nombreArchivo;

    std::ifstream archivo(nombreArchivo);
    
    if (!archivo.is_open()) {
        std::cout << "Error al abrir el archivo." << std::endl;
        return 1;
    }

    std::string linea;

    // Omitir la línea de encabezado
    std::getline(archivo, linea);
    
    std::vector<Empleado> empleados;

    while (std::getline(archivo, linea)) {
        std::istringstream iss(linea);
        std::string id, nombre, contraseña, puesto;

        std::getline(iss, id, ',');
        std::getline(iss, nombre, ',');
        std::getline(iss, contraseña, ',');
        std::getline(iss, puesto);

        Empleado empleado;
        empleado.id = id;
        empleado.nombre = nombre;
        empleado.contraseña = contraseña;
        empleado.puesto = puesto;

        empleados.push_back(empleado);
    }

    // Imprimir los datos capturados
    for (const auto& empleado : empleados) {
        std::cout << "ID: " << empleado.id << std::endl;
        std::cout << "Nombre: " << empleado.nombre << std::endl;
        std::cout << "Contraseña: " << empleado.contraseña << std::endl;
        std::cout << "Puesto: " << empleado.puesto << std::endl;
        std::cout << std::endl;
    }

    return 0;
}
