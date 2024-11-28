#include "node.h"
#include <stdio.h>
#include <stdlib.h>
#include <string>

using namespace std;

NodeCP::NodeCP(string nproyecto, string prioridad, string npy)
{
    this->nproyecto = nproyecto;
    this->prioridad = prioridad;
    this->npy = npy;
    this->next = NULL;
    this->prev = NULL;
}