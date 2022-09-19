from pickle import NONE
from turtle import pos
from Clases import Estudiante as est, listadoEst as lst
listaEst = lst()


def menu():
    print("1. Agregar Registro")
    print("2. Editar Registro")
    print("3. Eliminar Registro")
    print("4. Buscar por código")
    print("5. Mostrar registros")
    print("6. Buscar por nombre")
    print("7. Buscar por apellido")
    print("8. Buscar por carrera")
    print("10. Salir")
    op = int(input("Escriba su opcion: "))
    return op


def agregarRegistro():
    print("Agregar Datos del estudiante")
    codigo = input("Codigo: ")
    nombre = input("Nombre: ")
    apellidos = input("Apellidos: ")
    carrera = input("Carrera: ")
    resp = input("Posse Beca? SI - NO: ")
    if (resp.upper() == "SI"):
        beca = True
    else:
        beca = False
    estudiante = est(codigo, nombre, apellidos, carrera, beca)
    listaEst.agregarElemento(estudiante)


def modificarRegistro():
    print("Editar Registro")
    cod = input("Codigo: ")
    est, pos = listaEst.buscarElemento(cod)
    print(f"""Nombres Actual: {est.Nombres}
Apellidos actual: {est.Apellidos}
Carrera: {est.Carrera}
Beca: {est.Beca}""")
    print("Nuevos Datos")
    nuevoNombre = input("Nombres: ")
    nuevosApellidos = input("Apellidos: ")
    nuevaCarrera = input("Carrera: ")
    resp = input("Posse Beca? SI - NO")
    if (resp.upper() == "SI"):
        NuevaBeca = True
    else:
        NuevaBeca = False
    newEst = est(cod, nuevoNombre, nuevosApellidos, nuevaCarrera, NuevaBeca)
    listaEst.editarElemento(newEst,pos)

def eliminarRegistro():
    print("Eliminar registro")
    cod = input("Codigo: ")
    est, pos = listaEst.buscarElemento(cod)
    print(f"""Realmente desea Eliminar el registro {est}""")
    resp = input("SI-NO")
    if resp.upper() == "SI":
        listaEst.eliminarElemento(pos)
    else:
        print("Operación cancelada")

def buscarRegistros():
    print("Buscar registro")
    cod = input("Codigo: ")
    try:
        est, pos = listaEst.buscarElemento(cod)
    except:
        print("Todo bien")
    if est.Codigo != None: 
        print(est)

def buscarPorNombre():
    print("Buscar registro")
    nombre = input("Nombre: ")
    try: 
        est, pos = listaEst.buscarPorNombre(nombre)
    except: 
        print("Todo bien")
    if est.Nombre != None:
        print(est)

def buscarPorApellido():
    print("Buscar registro")
    apellido = input("Apellido: ")
    try: 
        est, pos = listaEst.buscarPorApellido(apellido)
    except: 
        print("Todo bien")
    if est.Apellido != None:
        print(est)

def buscarPorCarrera():
    print("Buscar registro")
    carrera = input("Carrera: ")
    try: 
        est, pos = listaEst.buscarPorCarrera(carrera)
    except: 
        print("Todo bien")
    if est.Carrera != None:
        print(est)

def mostrarRegistros():
    for estudiante in lst: 
        print(estudiante)
        print("="*30)

def main():
    op = 0;
    while(op != 10):
        op = menu()
        if op == 1: agregarRegistro()
        elif op == 2: modificarRegistro()
        elif op == 3: eliminarRegistro()
        elif op == 4: buscarRegistros()
        elif op == 5: mostrarRegistros()
        elif op == 6: buscarPorNombre()
        elif op == 7: buscarPorApellido()
        elif op == 8: buscarPorCarrera()
        elif op == 10: print("Ciao, ciao")
        else: print("Opcion no valida")

main()