from abc import ABC, abstractmethod
import pymongo
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

# Interfaces

class MHConsulter(ABC):

    @abstractmethod
    def getMonsterByName(self, nombre:str) -> Monstruo:
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

class MHWatcher(ABC):
    @abstractmethod
    def getSavedMonstruos(self) -> list:
        pass