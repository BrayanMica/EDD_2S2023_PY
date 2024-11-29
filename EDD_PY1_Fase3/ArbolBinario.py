# Python
import json
import os

# Clase Task para representar tareas
class Task:
    def __init__(self, codigo, proyecto, antecesores):
        self.codigo = codigo
        self.proyecto = proyecto
        self.antecesores = antecesores

# Función para generar las tareas a partir de los datos del JSON
def generate_tasks_from_json(json_data):
    tasks = {}
    proyectos = json_data["Tareas"]

    for proyecto_data in proyectos:
        codigo = proyecto_data["codigo"]
        proyecto = proyecto_data["proyecto"]
        antecesores = proyecto_data.get("antecesor", [])

        # Agregar la tarea a la lista de tareas
        tasks[codigo] = Task(codigo, proyecto, [antecesor["codigo"] for antecesor in antecesores])

    return tasks

# Función para generar el archivo .dot
def generate_dot_file(tasks, dot_filename):
    dot_content = []

    dot_content.append("digraph BinaryTree {\n")

    for task in tasks.values():
        dot_content.append(f'  "{task.codigo}" [label="{task.codigo}", fillcolor=lime, style=filled, color=blue];\n')
        for antecesor in task.antecesores:
            dot_content.append(f'  "{task.codigo}" -> "{antecesor}";\n')

    dot_content.append("}")

    dot_string = "".join(dot_content)

    with open(dot_filename, "w") as dot_file:
        dot_file.write(dot_string)

def generate_svg_file(data):
    
    # Generar las tareas
    tasks = generate_tasks_from_json(data)

    # Generar el archivo .dot
    dot_filename = "binary_tree.dot"
    generate_dot_file(tasks, dot_filename)

    # Generar el archivo .svg
    svg_filename = "binary_tree.svg"
    cmd = f"dot -Tsvg {dot_filename} -o {svg_filename}"
    os.system(cmd)
