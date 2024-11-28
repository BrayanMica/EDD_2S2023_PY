#include <string>
#pragma once

#ifndef _NODE_H_
#define _NODE_H_

using namespace std;
// Estructura de un nodo
class Node
{
public:
    int row;
    int col;
    string NombreFila;
    string NombreColumna;
    string val;
    Node *up;
    Node *down;
    Node *left;
    Node *right;
};

#endif // _NODE_H_