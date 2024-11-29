from typing import List
import typing
import hashlib
import os
import random
import webbrowser
cmd = "dot -Tsvg arbolMerkle-#proyecto.dot -o arbolMerkle-#proyecto.svg"

class Node:
    #Método constructor, recibe como parámetros el nodo izquierdo, derecho y el valor del nodo
    def __init__(self, left, right, value):
        self.left = left
        self.right = right
        self.value = value

    #Método para hacer la encrptación de los valores
    @staticmethod
    def _hash(value):
        return hashlib.sha256(value.encode()).hexdigest()

    #Método para hacer doble encrptación de los valores, para que sea más seguro
    @staticmethod
    def doubleHash(value):
        return Node._hash(Node._hash(value))

class MerkleTree:

    #Método constructor, recibe como parámetro una lista de valores y construye el árbol
    def __init__(self, values: List[str]) -> None:
        self.originalValues = values
        self.leaves = []
        self.__buildTree(values)
        self.randomVal = 1000

    #Método para iniciar la construcción del árbol
    def __buildTree(self, values: List[str]) ->Node:
        leaves: List[Node] =[Node(None, None, Node.doubleHash(value)) for value in values]
        if len(leaves) % 2 == 1:
            leaves.append(leaves[-1:][0]) # duplicate last elem if odd number of elements
        self.root: Node = self.__buildTreeRec(leaves)

    #Método complementario recursivo para construir el árbol
    def __buildTreeRec(self, nodes: List[Node])-> Node:
        half: int = len(nodes) // 2

        if len(nodes) == 2:
            return Node(nodes[0], nodes[1], Node.doubleHash(nodes[0].value + nodes[1].value))

        left: Node = self.__buildTreeRec(nodes[:half])
        right: Node = self.__buildTreeRec(nodes[half:])
        value: str = Node.doubleHash(left.value + right.value)
        return Node(left, right, value)

    #Método para imprimir el árbol
    def printTree(self)-> None:
        self.__printTreeRec(self.root)

    #Método complementario recursivo para imprimir el árbol
    def __printTreeRec(self, node)-> None:
        if node != None:
            print(node.value)
            self.__printTreeRec(node.left)
            self.__printTreeRec(node.right)

    #Método que expone el valor de la raíz del árbol
    def getRootHash(self)-> str:
        return self.root.value
    
    #Método para graficar el árbol
    def graphTree(self)-> None:
        dotContent = "digraph G {\nnode [shape=box]\n" + self.__graphTreeRec(self.root, random.randint(0,self.randomVal), "root") + "\n"

        for i in range(len(self.originalValues)):
            hashing = Node.doubleHash(self.originalValues[i])
            for j in range(len(self.leaves)):
                if hashing == self.leaves[j].get("value"):
                    randomNumber = random.randint(0, self.randomVal)
                    dotContent = dotContent + str(randomNumber) + "[label=\" {0} \n {1} \n {2} \n PY-100\" ,fillcolor=yellow, style=filled, color=red]\n".format(self.obtenerFechaHora(), self.originalValues[i], self.CodigoIdWallet())
                    dotContent = dotContent + self.leaves[j].get("index") + " -> " + str(randomNumber) + "\n"
                    break
                    
        dotContent = dotContent + "}"

        f = open("arbolMerkle-#proyecto.dot", "w")
        f.write(dotContent)
        f.close()
        os.system(cmd)
        # Abrir el archivo .svg
        webbrowser.open("arbolMerkle-#proyecto.svg")
    
    #Método complementario recursivo para graficar el árbol
    def __graphTreeRec(self, root, level, txt)-> None:
        if not root:
            return
        
        rootNode = txt + str(level) + "[label=\"{0}\",fillcolor=lime, style=filled, color=blue]\n".format(root.value)
        value = rootNode + "\n"

        randomNumber = random.randint(0, self.randomVal)

        leftNode = self.__graphTreeRec(root.left, randomNumber, "left")
        rightNode = self.__graphTreeRec(root.right, randomNumber, "right")

        if root.left:
            value += txt + str(level) + " -> {0}\n".format("left" + str(randomNumber)) + leftNode
        if root.right:
            value += txt + str(level) + " -> {0}\n".format("right" + str(randomNumber)) + rightNode
        
        if root.left == None and root.right == None:
            self.leaves.append({"value": root.value, "index": txt + str(level)})

        return value
    #funcion obtener hora y fecha actual
    def obtenerFechaHora(self):
        from datetime import datetime
        now = datetime.now()
        fechaHora = now.strftime("%d/%m/%Y %H:%M:%S")
        return fechaHora
    
    def CodigoIdWallet(self):
        idWallet = random.randint(0, 999)
        return idWallet

# def test()-> None:
#     elems = ["L1", "L2", "L3", "L4", "L5", "L6", "L7"]
#     mtree = MerkleTree(elems)
#     #mtree.printTree()
#     mtree.graphTree()

# if __name__ == "__main__":
#     test()

