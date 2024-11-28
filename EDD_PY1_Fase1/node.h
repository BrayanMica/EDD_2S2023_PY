#pragma once

#ifndef NODE_H
#define NODE_H
#include <string>

class NodeCP
{
public:
    std::string nproyecto;
    std::string prioridad;
    std::string npy;
    NodeCP *next;
    NodeCP *prev;
    NodeCP(std::string nproyecto, std::string prioridad, std::string npy);
};

#endif // !NODE_H