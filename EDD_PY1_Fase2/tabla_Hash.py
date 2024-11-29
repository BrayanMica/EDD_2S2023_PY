class Empleado:
    def __init__(self, id, nombre, contrasenia):
        self.id = id
        self.nombre = nombre
        self.contrasenia = contrasenia

    def __str__(self):
        return f"ID: {self.id} - Nombre: {self.nombre} - Contraseña: {self.contrasenia}"

class TablaHash:
    def __init__(self, tamanio):
        self.tabla = [None] * tamanio
        self.factorCarga = 0

    def __str__(self):
        data = ""
        for i in range(len(self.tabla)):
            if self.tabla[i] != None:
                data += f"{i} - {self.tabla[i]}\n"
            else:
                data += f"{i} - {self.tabla[i]}\n"
        return data

    def toInt(self, name):
        value = 0
        for character in name:
            value += ord(character)
        return value

    def getNextFibonacci(self, n):
        a, b = 0, 1
        while b < n:
            a, b = b, a + b
        return b

    def funcionHash(self, clave, busqueda=False):
        hash = self.toInt(clave) % len(self.tabla)

        if busqueda:
            if self.tabla[hash] and self.tabla[hash].nombre == clave:
                return hash

        if self.tabla[hash] != None:
            hash = self.colisionHash(hash, busqueda, clave)

        return hash

    def colisionHash(self, hash, busqueda, clave, extra=0):
        nuevoHash = hash
        cuadratico = 0
        while nuevoHash < len(self.tabla) and self.tabla[nuevoHash] != None:
            nuevoHash = nuevoHash + pow(cuadratico, 2) + extra
            if busqueda and nuevoHash < len(self.tabla):
                if self.tabla[nuevoHash] and self.tabla[nuevoHash].nombre == clave:
                    return nuevoHash

            cuadratico += 1

        if nuevoHash >= len(self.tabla):
            nuevoHash = self.colisionHash(0, busqueda, clave, 1)

        return nuevoHash

    def rehashing(self):
        nuevaTabla = TablaHash(self.getNextFibonacci(len(self.tabla) + 1))
        for i in range(len(self.tabla)):
            if self.tabla[i] != None:
                nuevaTabla.set(self.tabla[i].nombre, self.tabla[i])
        self.tabla = nuevaTabla.tabla

    def set(self, clave, valor):
        while self.factorCarga / len(self.tabla) > 0.7:
            self.rehashing()

        direccion = self.funcionHash(clave)

        self.tabla[direccion] = valor
        self.factorCarga += 1

    def get(self, clave):
        direccion = self.funcionHash(clave, True)
        return self.tabla[direccion]

def main():
    usuarios = TablaHash(5)