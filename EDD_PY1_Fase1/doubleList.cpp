#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include "node.h"
#include "doubleList.h"

using namespace std;
// Variables globales

DoubleList::DoubleList()
{
    this->head = NULL;
}

NodeCP* DoubleList::search(string prioridad)
{
    NodeCP* current = this->head;
    while (current != nullptr)
    {
        if (current->prioridad == prioridad)
        {
            return current;
        }
        current = current->next;
    }
    return nullptr;
}

void DoubleList::add(std::string nproyecto, std::string prioridad, std::string npy)
{   
    //NodeCP *search = this->search(prioridad);
    //if (search != NULL)
    //{
        //std::cout<<"El valor "<<prioridad<<" ya existe en la lista\n";
    //    return;
    //}


    NodeCP *newNode = new NodeCP(nproyecto, prioridad, npy);
    if (this->head == NULL)
    {
        this->head = newNode;
    }
    else
    {
        NodeCP *current = this->head;
        while (current->next != NULL)
        {
            current = current->next;
        }
        current->next = newNode;
        newNode->prev = current;
    }
    this->sortAsc();
    printf("Creado Exitosamente, %s\n",npy.c_str());
    //printf("Proyecto %s %s y Prioridad %s fue creado. \n",nproyecto.c_str(),npy.c_str(),prioridad.c_str());
}

bool DoubleList::verificarNpy(std::string codex) {
    NodeCP* current = this->head;
    while (current != NULL) {
        if (current->npy == codex) {
            return true;
        }
        current = current->next;
    }
    return false;
}

string DoubleList:: buscarPrioridadPorNpy(std::string valor) {
    NodeCP *current = this->head;
    while (current != NULL) {
        if (current->npy == valor) {
            return current->prioridad;
        }
        current = current->next;
    }
    return ""; // Si no se encuentra ningún nodo con ese npy, se devuelve una cadena vacía
}

void DoubleList::sortAsc()
{
    NodeCP *current = this->head;
    NodeCP *index = NULL;
    string temp;

    if (this->head == NULL)
    {
        return;
    }
    else
    {
        while (current != NULL)
        {
            index = current->next;

            while (index != NULL)
            {
                if (current->prioridad.compare(index->prioridad) > 0)
                {
                    temp = current->nproyecto;
                    current->nproyecto = index->nproyecto;
                    index->nproyecto = temp;
                    printf("%s \n",current->nproyecto.c_str());
                    temp = "";
                    temp = current->prioridad;
                    current->prioridad = index->prioridad;
                    printf("%s \n",current->prioridad.c_str());
                    index->prioridad = temp;
                    temp = "";
                    temp = current->npy;
                    current->npy = index->npy;
                    printf("%s \n",current->npy.c_str());
                    index->npy = temp;
                    temp = "";
                }
                index = index->next;
            }
            current = current->next;
        }
    }
}

void DoubleList::generateGraphvizFile(string fileName)
{
    FILE *file;
    string fileNameWithExtension = fileName + ".dot";
    file = fopen(fileNameWithExtension.c_str(), "w");
    if (file != NULL)
    {
        string text = "digraph G {\n";
        string Cnodos = "";
        text += "rankdir=LR\nnode [shape=box];\n";

        NodeCP *current = this->head;
        while (current != NULL)
        {
            text += current->nproyecto + current->prioridad + "[label=\"" + current->nproyecto + "\n" + current->npy + "\nPrioridad" + current->prioridad + "\"];\n";  
            if (current->next != NULL)
            {
                Cnodos += current->nproyecto + current->prioridad + "->";
            }else{
                Cnodos += current->nproyecto + current->prioridad;
            }
            
            
            current = current->next;
        }
        text +=Cnodos;
        text += "[dir=back];\n}";
        fputs(text.c_str(), file);
        fclose(file);

        string command = "dot -Tpng " + fileNameWithExtension + " -o " + fileName + ".png";
        system(command.c_str());
    }
    else
    {
        printf("Error al generar el archivo\n");
    }
}