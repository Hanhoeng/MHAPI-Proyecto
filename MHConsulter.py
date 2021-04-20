from abc import ABC, abstractmethod
from pymongo import MongoClient
import requests as peticion
import json

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

# Interfaces

class MHConnector(ABC):
    host = "localhost"
    port = 27017
    MongoClient(host,port)

class MHConsulter(ABC):

    @abstractmethod
    def getMonsterByName(self, nombre:str) -> Monstruo:
        conector = MHConnector()

        pass

    @abstractmethod
    def getMonsterByDebilidad(self, debilidad:str) -> Monstruo:
        pass

    @abstractmethod
    def getMonsterByResistencia(self, resistencia:str) -> Monstruo:
        pass

class MHRecorder(ABC):

    @abstractmethod
    def setMonstruo(self, monstruo:Monstruo) -> bool:
        pass

    @abstractmethod
    def checkIfExist(self, monstruo:Monstruo) -> bool:
        pass

class MHWatcher(ABC):
    @abstractmethod
    def getSavedMonstruos(self) -> list:
        pass