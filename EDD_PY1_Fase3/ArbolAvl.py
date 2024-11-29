import os

cmd = "dot -Tpng avlTree.dot -o avlTree.png"

class treeNode(object):
    def __init__(self, project_id, project_name, priority):
        self.project_id = project_id
        self.project_name = project_name
        self.priority = priority
        self.value = self.calculate_hash(project_id)
        self.l = None
        self.r = None
        self.h = 1

    def calculate_hash(self, project_id):
        parts = project_id.split('-')
        if len(parts) == 2:
            prefix = parts[0]
            number = int(parts[1])
            value = 0
            for character in prefix:
                value += ord(character)
            value += number
            return value
        else:
            value = 0
            for character in str(project_id):
                value += ord(character)
            return value

class AVLTree(object):
    def insert(self, root, project_id, project_name, priority):

        if not root:
            return treeNode(project_id, project_name, priority)

        if project_id == root.project_id:
            project_id = self.handle_collision(root, project_id)

        if project_id < root.project_id:
            root.l = self.insert(root.l, project_id, project_name, priority)
        else:
            root.r = self.insert(root.r, project_id, project_name, priority)

        root.h = 1 + max(self.getHeight(root.l), self.getHeight(root.r))

        b = self.getBal(root)

        if b > 1 and project_id < root.l.project_id:
            return self.rRotate(root)

        if b < -1 and project_id > root.r.project_id:
            return self.lRotate(root)

        if b > 1 and project_id > root.l.project_id:
            root.l = self.lRotate(root.l)
            return self.rRotate(root)

        if b < -1 and project_id < root.r.project_id:
            root.r = self.rRotate(root.r)
            return self.lRotate(root)

        return root

    def handle_collision(self, root, project_id):
        new_project_id = self.generate_new_id(root, project_id)
        while self.search(root, new_project_id):
            new_project_id = self.generate_new_id(root, new_project_id)
        return new_project_id

    def generate_new_id(self, root, project_id):
        existing_ids = self.collect_ids(root)
        prefix = project_id.split("-")[0]
        num = int(project_id.split("-")[1])
        num += 1
        new_id = f"{prefix}-{num:03}"
        while new_id in existing_ids:
            num += 1
            new_id = f"{prefix}-{num:03}"
        return new_id

    def collect_ids(self, root):
        ids = []
        if root:
            ids.append(root.project_id)
            ids.extend(self.collect_ids(root.l))
            ids.extend(self.collect_ids(root.r))
        return ids

    def search(self, root, project_id):
        if not root:
            return False
        if project_id == root.project_id:
            return True
        if project_id < root.project_id:
            return self.search(root.l, project_id)
        else:
            return self.search(root.r, project_id)

    def lRotate(self, z):

        y = z.r
        T2 = y.l

        y.l = z
        z.r = T2

        z.h = 1 + max(self.getHeight(z.l), self.getHeight(z.r))
        y.h = 1 + max(self.getHeight(y.l), self.getHeight(y.r))

        return y

    def rRotate(self, z):

        y = z.l
        T3 = y.r

        y.r = z
        z.l = T3

        z.h = 1 + max(self.getHeight(z.l), self.getHeight(z.r))
        y.h = 1 + max(self.getHeight(y.l), self.getHeight(y.r))

        return y

    def getHeight(self, root):
        if not root:
            return 0

        return root.h

    def getBal(self, root):
        if not root:
            return 0

        return self.getHeight(root.l) - self.getHeight(root.r)

    def preOrder(self, root):

        if not root:
            return

        print("ID: {0}, Proyecto: {1}, Prioridad: {2}, Valor: {3}".format(root.project_id, root.project_name, root.priority, root.value))
        self.preOrder(root.l)
        self.preOrder(root.r)

    def export_graphviz(self, root):
        dotContent = "digraph G {\n"
        auxContent = self.aux_export_graphviz(root) if root else ""
        if auxContent:
            dotContent += auxContent
        dotContent += "}"
        f = open("avlTree.dot", "w")
        f.write(dotContent)
        f.close()
        os.system(cmd)

    def aux_export_graphviz(self, root):
        if not root:
            return ""

        leftNode = self.aux_export_graphviz(root.l)
        rightNode = self.aux_export_graphviz(root.r)

        rootNode = "node{0}".format(root.value) + \
            "[label=\"ID: {0}\\nProyecto: {1}\\nPrioridad: {2}\\nValor: {3}\\nAltura: {4}\\nBalance: {5}\", shape=\"box\"]\n".format(
                root.project_id, root.project_name, root.priority, root.value, root.h, self.getBal(root))

        value = rootNode + "\n"

        if root.l:
            value += "node{0}".format(root.value) + \
                " -> node{0}\n".format(root.l.value) + leftNode
        if root.r:
            value += "node{0}".format(root.value) + \
                " -> node{0}\n".format(root.r.value) + rightNode

        return value

