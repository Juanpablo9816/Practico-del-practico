class Persona:
    __dni=None
    __apellidoNombre=None
    __categoria=None
    __rol=None
    def __init__(self, dni, apellidoNombre, categoria, rol):
        self.__dni=dni
        self.__apellidoNombre=apellidoNombre
        self.__categoria=categoria
        self.__rol=rol
    def getCategoria(self):
        return self.__categoria
    def getRol(self):
        return self.__rol
    def __str__(self):
        '''devuelve una representación en una cadena con los datos de la persona'''
        p="Apellido y Nombre: ",self.__apellidoNombre +"\n"
        p+="DNI: ",self.__dni +'\n'
        p+="Categoria: ",self.__categoria +'\n'
        p+="Rol: ",self.__rol +'\n'
        return p
        