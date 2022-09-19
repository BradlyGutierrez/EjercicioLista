#Crear una lista de estudiantes 


from turtle import pos


class Estudiante:
    def __init__(self, cod, nom, ape, car, bec):
        self.Codigo = cod; 
        self.Nombre = nom; 
        self.Apellido = ape; 
        self.Carrera = car; 
        self.Becado = bec; #Becado será un valor booleano 

    def __str__(self):
        return f"""Código:{self.Codigo}
Nombres: {self.Nombre}
Apellidos:{self.Apellido}
Carrera: {self.Carrera}
Beca: {self.Becado}
"""

class listadoEst:
    def __init__(self):
        self.lista = []
    def agregarElemento(self, dato):
        try:
            self.lista.append(dato)
        except Exception as ex:
            print("Ocurrió un error inesperado", str(ex))
    def editarElemento(self, dato, pos):
        try:
            self.lista[pos] = dato
        except Exception as ex: 
            print("Ocurrio un error al editar", str(ex))
    def eliminarElemento(self, pos):
        try:
            self.lista.remove(pos)
        except Exception as ex: 
            print("Error al eliminar: ", str(ex))
    
    def buscarElemento(self,cod):
        try: 
            for est in self.lista:
                if est.Codigo == cod:
                    print("Estudiante encontrado")
                    return est, pos
            else:
                print("No se encontro el estudiante")
        except Exception  as ex: 
            print("Error al buscar", str(ex)) 
    
    def buscarPorNombre(self,nom):
        try: 
            for est in self.lista:
                if est.Nombre == nom:
                    print("Estudiante encontrado")
                    return est, pos
            else: 
                print("No se encontró el estudiante")
        except Exception as ex:
            print("Error al buscar", str(ex))    

    def buscarPorApellido(self,ape):
        try: 
            for est in self.lista:
                if est.Apellido == ape:
                    print("Estudiante encontrado")
                    return est, pos
            else: 
                print("No se encontró el estudiante")
        except Exception as ex:
            print("Error al buscar", str(ex))     

    def buscarPorCarrera(self,carre):
        try: 
            for est in self.lista:
                if est.Carrera == carre:
                    print("Estudiante encontrado")
                    return est, pos
            else: 
                print("No se encontró el estudiante")
        except Exception as ex:
            print("Error al buscar", str(ex))