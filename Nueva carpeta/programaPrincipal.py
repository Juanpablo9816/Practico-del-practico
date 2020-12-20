from claseManejadorProyectos import ManejadorProyectos
from claseProyecto import Proyecto
from clasePersona import Persona
from claseManejadorPersonas import ManejadorPersonas
import csv
def item1(manejador):
    archivo = open("proyectos.csv")
    leer = csv.reader(archivo, delimiter = ";")
    bandera = 0
    for proyectos in leer:
        if bandera == 0:
            bandera = 1
        else:
            manejador.agregarProyecto(Proyecto(proyectos[0],proyectos[1],proyectos[2]))
    archivo.close()
def item2(manejador):
    archivo = open("integrantesProyecto.csv")
    leer = csv.reader(archivo,delimiter = ";")
    bandera = 0
    for integrante in leer:
        if bandera == 0:
            bandera = 1
        else:
            manejador.agregarPersonaProyecto(integrante[0],Persona(integrante[2],integrante[1],integrante[3],integrante[4]))
    archivo.close()
def item3(manejador): 
    '''calcular el puntaje de los proyectos'''
    '''ordenar los proyectos por puntaje'''
    '''mostrar el rankin de proyectos, ordenados por puntaje'''
    print('Listado de Proyectos (rankin por puntaje)')
    print('--------------------')
    manejador.mostrarProyectos()
if __name__=='__main__':
    manejadorProyectos = ManejadorProyectos()
    item1(manejadorProyectos)
    item2(manejadorProyectos)
    item3(manejadorProyectos)
