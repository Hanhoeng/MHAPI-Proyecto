from abc import ABC, abstractmethod

# Entidades
## Monstruos
class Monstruo():
    def __init__(self, nombre:str,debilidades:list,resistencia:str,descripcion:str):
        self.nombre = nombre
        self.debilidades = debilidades
        self.resistencia = resistencia
        self.descripcion = descripcion

    def __str__(self) -> str:
        self.cadena = "Nombre: {}\n".format(self.nombre)
        self.cadena += "Debilidades: {}\n".format(self.debilidades)
        self.cadena += "resistencia: {}\n".format(self.resistencia)
        self.cadena += "descripción: {}\n".format(self.descripcion)
        return self.cadena
        
class MHRecorder(ABC):

    @abstractmethod
    def setConnection(self, host:str, port:int) -> bool:
        pass

    @abstractmethod
    def setMonstruo(self, monstruo:Monstruo) -> bool:
        pass

    @abstractmethod
    def checkIfExist(self, monstruo:Monstruo) -> bool:
        pass

    @abstractmethod
    def getSavedMonstruos(self) -> list:
        pass