#pragma once

#ifndef _MATRIX_H_
#define _MATRIX_H_

#include "nodeDispersa.h"

using namespace std;

class SparseMatrix
{
public:
    // constructor
    SparseMatrix();

    // create node
    Node *createNode(int row, int col,string NombreFila,string NombreColumna, string val);

    // get dot of the matrix
    void getGraphviz();

private:
    Node *head;

    // create node for vertical head
    Node *createVertHead(int row);

    // create node for horizontal head
    Node *createHorzHead(int col);

    // search head in horz
    Node *searchHorzHead(int col);

    // search head in vert
    Node *searchVertHead(int row);
};

#endif // _MATRIX_H_