from claseManejadorPersonas import ManejadorPersonas
class Proyecto:
    __idProyecto=None
    __titulo=None
    __palabrasClave=None
    '''__integrantes es una instancia de ManejadorPersonas'''
    __integrantes=None
    __puntaje=None
    def __init__(self, idProyecto, titulo, palabrasClave):
        '''crea un proyecto a partir de los datos recibidos'''
        self.__idProyecto=idProyecto
        self.__titulo=titulo
        self.__palabrasClave=palabrasClave
        self.__integrantes=ManejadorPersonas()
    def getIdProyecto(self):
        '''devuelve el idProyecto'''
        return self.__idProyecto
    def agregarIntegrante(self, persona):
        '''agrega una Persona al manejador de Personas (__integrantes)'''
        self.__integrantes.agregarPersona(persona)
    def setPuntaje(self, puntaje):
        '''establece el valor del puntaje al atributo __puntaje'''
        self.__puntaje=puntaje
    def getPuntaje(self):
        '''devuelve el valor del __puntaje del Proyecto'''
        return self.__puntaje
    def calcularPuntaje(self):
        print('Cálculo de puntajes')
        print('-------------------')
        '''imprimr datos del ¨Proyecto'''
        '''luego realizar cálculo de puntaje'''
        pass
    def __gt__(self, otroProyecto):
        '''utilizado para ordenar de mayor a menor los Proyectos, según el puntaje obtenido'''
        pass
    def __str__(self):
        '''devuelve una cadena con los datos del Proyecto y de los integrantes del mismo'''
        p="**************DATOS DEL PROYECTO**************" + "\n"
        p+="id Proyecto: {}".format(str(self.__idProyecto)) + "\n"
        p+="Titulo: {}".format(str(self.__titulo)) + "\n"
        p+="Palabras Clave: {}".format(str(self.__palabrasClave)) + "\n"
        p+="**************INTEGRANTES**************" + "\n"
        cant=self.__integrantes.getCantidadIntegrantes()
        for i in range(cant):
            pers = "\n{}" .format(self.__integrantes.getPersona(i))
            p += pers.__str__()
        return p

        