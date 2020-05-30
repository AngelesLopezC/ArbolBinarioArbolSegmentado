class Nodo:
    def __init__(self, nombre=None, edad=None, izq=None, der=None):
        self.nombre = nombre
        self.edad   = edad
        self.izq    = izq
        self.der    = der

    def str(self):
        return "%s %s" %(self.nombre, self.edad)


class segmentado:
    def __init__(self):
        self.raiz = None

    def agregar(self, elemento):
        if self.raiz  == None:
            self.raiz = elemento
        else:
            aux = self.raiz
            padre = None
            while aux != None:
                padre = aux
                if int(elemento.edad) >= int(aux.edad):
                    aux = aux.der
                else:
                    aux = aux.izq
            if int(elemento.edad) >= int(padre.edad):
                padre.der = elemento
            else:
                padre.izq = elemento

    def preorden(self, elemento):
        if elemento != None:
            print(elemento.str())
            self.preorden(elemento.izq)
            self.preorden(elemento.der)

    def postorden(self, elemento):
        if elemento != None:
            self.postorden(elemento.izq)
            self.postorden(elemento.der)
            print(elemento.str())

    def inorden(self, elemento):
        if elemento != None:
            self.inorden(elemento.izq)
            print(elemento.str())
            self.inorden(elemento.der)

    def getRaiz(self):
        return self.raiz


if __name__ == "__main__":
    Arbol = segmentado()
    while(True):
        print("---Menu---\n"+"1. Agregar"+"\n"+"2. Raiz")
        num = input("Ingrese la opcion: ")
        if num == "1":
            nombre = input("Ingrese nombre: ")
            edad = input("Ingrese la edad: ")
            nod = Nodo(nombre, edad)
            Arbol.agregar(nod)
        else:
            print("listo")
            break


