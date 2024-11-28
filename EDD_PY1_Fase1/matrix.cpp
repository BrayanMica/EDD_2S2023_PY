#include <stdio.h>
#include <stdlib.h>
#include "matrix.h"
#include "nodeDispersa.h"
#include <string>

using namespace std;

// get string if value is -1 
string getVal(int valor)
{
    if (valor == -1)
    {
        return "head";
    }
    return to_string(valor);
}

// constructor
SparseMatrix::SparseMatrix()
{
    head = new Node;
    head->row = -1;
    head->col = -1;

    head->NombreFila = "";
    head->NombreColumna = "";
    head->val = "";

    // conexiones de nodo
    head->up = NULL;
    head->down = NULL;
    head->left = NULL;
    head->right = NULL;
}

// create node
Node *SparseMatrix::createNode(int row, int col,std::string NombreFila,std::string NombreColumna, std::string val)
{
    Node *newNode = new Node;
    newNode->row = row;
    newNode->col = col;

    newNode->NombreFila = NombreFila;
    newNode->NombreColumna = NombreColumna;
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
        {
            break;
        }
        temp = temp->right;
        temp3 = temp3->right;
    }
    
    // Busqueda vetical e insercion
    while (temp4 != NULL)
    {
        if (temp4->row > row)
        {
            break;
        }
        temp2 = temp2->down;
        temp4 = temp4->down;
    }

    // Apuntando el nuevo nodo a los nodos adyacentes de la matriz dispersa
    newNode->right = temp3;
    newNode->left = temp;
    newNode->up = temp2;
    newNode->down = temp4;

    if (temp3 != NULL)
    {
        temp3->left = newNode;
    }
    if (temp4 != NULL)
    {
        temp4->up = newNode;
    }
    temp->right = newNode;
    temp2->down = newNode;

    return newNode;
}
// get dot of the matrix
// reference to matrix dot: https://stackoverflow.com/questions/49343366/graphviz-sparse-matrix-node-aligment
void SparseMatrix ::getGraphviz()
{
    FILE *fp;
    fp = fopen("graphviz.dot", "w+");

    fprintf(fp, "digraph G {\n");
    fprintf(fp, "node [shape=box];\n");

    /// add group 1 for vertical alignment
    fprintf(fp, "Mt[ label =\"Cabeza\", width = 1.5, style = filled, fillcolor = firebrick1, group = 1 ];\n");

    // empty nodes, needed to override graphiz' default node placement
    fprintf(fp, "e0[ shape = point, width = 0 ];\n");
    fprintf(fp, "e1[ shape = point, width = 0 ];\n");

    // create row headers
    Node *temp = head->down;
    if (temp != NULL)
    {
        fprintf(fp, "Mt -> node%s%s%s;\n", getVal(temp->row).c_str(), getVal(temp->col).c_str(), temp->val.c_str());
    }
    while (temp != NULL)
    {
        fprintf(
            fp, "node%s%s%s [label=\"F%d\" width = 1.5 style = filled, fillcolor = bisque1, group = 1];\n",
            getVal(temp->row).c_str(), getVal(temp->col).c_str(),
            temp->val.c_str(), temp->row);

        if (temp->down != NULL)
        {
            fprintf(
                fp, "node%s%s%s -> node%s%s%s;\n",
                getVal(temp->row).c_str(), getVal(temp->col).c_str(),
                temp->val.c_str(), getVal(temp->down->row).c_str(),
                getVal(temp->down->col).c_str(), temp->down->val.c_str());
        }

        temp = temp->down;
    }

    // create column headers
    temp = head->right;
    int count = 1000;
    if (temp != NULL)
    {
        fprintf(fp, "Mt -> node%s%s%s;\n", getVal(temp->row).c_str(), getVal(temp->col).c_str(), temp->val.c_str());
    }
    string additionalTextCol = "{ rank = same; Mt; ";
    while (temp != NULL)
    {
        additionalTextCol += "node" + getVal(temp->row) + getVal(temp->col) + temp->val + "; ";
        fprintf(
            fp,
            "node%s%s%s [label=\"C%d \" width = 1.5 style = filled, fillcolor = lightskyblue, group = %d ];\n",
            getVal(temp->row).c_str(), getVal(temp->col).c_str(),
            temp->val.c_str(), temp->col, count);

        if (temp->right != NULL)
        {
            fprintf(
                fp, "node%s%s%s -> node%s%s%s;\n",
                getVal(temp->row).c_str(), getVal(temp->col).c_str(),
                temp->val.c_str(), getVal(temp->right->row).c_str(),
                getVal(temp->right->col).c_str(), temp->right->val.c_str());
        }

        temp = temp->right;
        count++;
    }
    additionalTextCol += "};\n";
    fprintf(fp, "%s", additionalTextCol.c_str());

    // create internal nodes
    temp = head->down;
    while (temp != NULL)
    {
        Node *temp2 = temp->right;
        while (temp2 != NULL)
        {
            fprintf(
                fp,
                "node%s%s%s [label=\"%s \" width = 1.5, group = %d ];\n",
                getVal(temp2->row).c_str(), getVal(temp2->col).c_str(),
                temp2->val.c_str(), temp2->val.c_str(), temp2->col + 1000);

            temp2 = temp2->right;
        }
        temp = temp->down;
    }

    // create releationships
    temp = head->down;
    while (temp != NULL)
    {
        string additionalTxt = "{ rank = same; ";
        Node *temp2 = temp;
        int count = 0;
        while (temp2 != NULL)
        {
            additionalTxt += "node" + getVal(temp2->row) + getVal(temp2->col) + temp2->val.c_str() + "; ";
            // right relationships
            if (temp2->right != NULL)
            {
                fprintf(
                    fp, "node%s%s%s -> node%s%s%s;\n",
                    getVal(temp2->row).c_str(), getVal(temp2->col).c_str(),
                    temp2->val.c_str(), getVal(temp2->right->row).c_str(),
                    getVal(temp2->right->col).c_str(), temp2->right->val.c_str());
            }
            // up relationships
            if (temp2->up != NULL && count > 0)
            {
                fprintf(
                    fp, "node%s%s%s -> node%s%s%s;\n",
                    getVal(temp2->up->row).c_str(), getVal(temp2->up->col).c_str(),
                    temp2->up->val.c_str(), getVal(temp2->row).c_str(),
                    getVal(temp2->col).c_str(), temp2->val.c_str());
            }

            temp2 = temp2->right;
            count++;
        }
        temp = temp->down;
        additionalTxt += "};\n";
        fprintf(fp, "%s", additionalTxt.c_str());
    }

    fprintf(fp, "}\n");

    fclose(fp);
    system("dot -Tpng graphviz.dot -o graphviz.png");
}

// search head in horz
Node *SparseMatrix::searchHorzHead(int col)
{
    Node *temp = head;
    while (temp != NULL)
    {
        if (temp->col == col)
        {
            return temp;
        }
        temp = temp->right;
    }
    return NULL;
}

// create node for horizontal head
Node *SparseMatrix ::createHorzHead(int col)
{
    Node *newNode = searchHorzHead(col);
    if (newNode != NULL)
    {
        return newNode;
    }

    newNode = new Node;
    newNode->row = -1;
    newNode->col = col;
    newNode->NombreFila= "";
    newNode->NombreColumna="";
    newNode->val = "";
    newNode->up = NULL;
    newNode->down = NULL;
    newNode->left = NULL;
    newNode->right = NULL;

    Node *temp = head;
    // insert in order
    while (temp->right != NULL)
    {
        if (temp->right->col > col)
        {
            break;
        }
        temp = temp->right;
    }
    newNode->right = temp->right;
    temp->right = newNode;

    return newNode;
}

// search head in vert
Node *SparseMatrix::searchVertHead(int row)
{
    Node *temp = head;
    while (temp != NULL)
    {
        if (temp->row == row)
        {
            return temp;
        }
        temp = temp->down;
    }
    return NULL;
}

// create node for vertical head
Node *SparseMatrix ::createVertHead(int row)
{
    Node *newNode = searchVertHead(row);
    if (newNode != NULL)
    {
        return newNode;
    }

    newNode = new Node;
    newNode->row = row;
    newNode->col = -1;
    newNode->NombreFila="";
    newNode->NombreColumna="";
    newNode->val = "";
    newNode->up = NULL;
    newNode->down = NULL;
    newNode->left = NULL;
    newNode->right = NULL;

    Node *temp = head;
    // insert in order
    while (temp->down != NULL)
    {
        if (temp->down->row > row)
        {
            break;
        }
        temp = temp->down;
    }
    newNode->down = temp->down;
    temp->down = newNode;

    return newNode;
}