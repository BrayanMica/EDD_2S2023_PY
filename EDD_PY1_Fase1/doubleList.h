#pragma once

#ifndef DOUBLELIST_H
#define DOUBLELIST_H

#include "node.h"
#include <string>

using namespace std;

class DoubleList
{
public:
    DoubleList();
    void add(string nproyecto, string prioridad, string npy);
    //void remove(string prioridad);
    bool verificarNpy(string codex);
    string buscarPrioridadPorNpy(string valor);
    void generateGraphvizFile(string fileName);

private:
    NodeCP *head;
    void sortAsc();
    NodeCP *search(string prioridad);
};

#endif // !DOUBLELIST_H