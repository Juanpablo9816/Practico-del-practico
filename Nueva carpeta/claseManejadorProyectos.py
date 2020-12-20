from claseProyecto import Proyecto
class ManejadorProyectos:
    __proyectos=None
    def __init__(self):
        self.__proyectos=[]
    def agregarProyecto(self, proyecto):
        '''recibe un objeto proyecto a agregar a la colección'''
        self.__proyectos.append(proyecto)
    def mostrarProyectos(self):
        '''recorre la colección de proyectos, muestra los datos de proyecto y personas integrantes'''
        for proye in self.__proyectos:    
            print(proye)
    def buscarProyectoPorId(self, idProyecto):
        '''dado un idProyecto, lo busca en la colección, si lo encuentra devuelve el proyecto, si no lo encuentra, devuelve una referencia None'''
        i=0
        while i<len(self.__proyectos) and idProyecto!=self.__proyectos[i].getIdProyecto():
            i+=1
        if i<len(self.__proyectos):
            return i
        else:
            return None
    def agregarPersonaProyecto(self, idProyecto, persona):
        '''recibe un idProyecto, y una persona a agregar a dicho Proyecto'''
        '''hace uso del método buscarProyectoPorId para buscar el Proyecto'''
        pos=self.buscarProyectoPorId(idProyecto)
        if pos!=None:
            self.__proyectos[pos].agregarIntegrante(persona)
        else:
            print("No existe le preyecto")
    def calcularPuntajeProyectos(self):
        '''para cada Proyecto de la colección, calcula el puntaje según reglas de negocio'''
        
    def ordenarProyectosPorPuntaje(self):
        '''invoca a la función sort de las lista, que hace uso del operador sobrecargado en la clase Proyecto __gt__'''
        self.__proyectos.sort()