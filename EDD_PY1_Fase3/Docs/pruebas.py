import json

json_string = """
{
    "Tareas":[
        {
            "proyecto" : "PY-100",
            "codigo" : "T1-PY-100",
            "antecesor" : [],
            "pago" : "152"
        },
        {
            "proyecto" : "PY-100",
            "codigo" : "T2-PY-100",
            "antecesor" : [],
            "pago" : "162"
        },
        {
            "proyecto" : "PY-100",
            "codigo" : "T3-PY-100",
            "antecesor" : [
                {
                    "codigo" : "T2-PY-100"
                },
                {
                    "codigo" : "T1-PY-100"
                }

            ],
            "pago" : "222"
        },
        {
            "proyecto" : "PY-100",
            "codigo" : "T4-PY-100",
            "antecesor" : [
            ],
            "pago" : "125"
        }
    
    ]
}
"""

data = json.loads(json_string)

# Ahora, 'data' es un diccionario que contiene los datos del objeto JSON
print(data)