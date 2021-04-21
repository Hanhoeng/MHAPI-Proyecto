from re import S
from pymongo import MongoClient
from abc import ABC, abstractmethod

# Entidades
## Monstruos
class Monstruo():
    def __init__(self, nombre:str,debilidades:list,resistencia:list,descripcion:str):
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

class MHConsulterBuscador(MHConsulter):
    ### ATENCION AQUI: poner el puerto de tu base de mongo
    mongo_client = MongoClient(host="localhost",port=27017)
    db = mongo_client["MHConsulter"]
    col = db["Monster"]

    def getMonsterByName(self, nombre: str):
        resultado = (self.col).find({},{"name":nombre})
        name = resultado["name"]
        descripcion = resultado["Descripcion"]
        weakness = resultado["weakness"]
        resistances = resultado["resistances"]
        monstruo = Monstruo(name,weakness,resistances,descripcion)
        return monstruo

    def getMonsterByDebilidad(self, debilidad: str):
        resultado = (self.col).find({},{"weakness":debilidad})
        name = resultado["name"]
        descripcion = resultado["Descripcion"]
        weakness = resultado["weakness"]
        resistances = resultado["resistances"]
        monstruo = Monstruo(name,weakness,resistances,descripcion)
        return monstruo

    def getMonsterByResistencia(self, resistencia: str):
        resultado = (self.col).find({},{"resistances":resistencia})
        name = resultado["name"]
        descripcion = resultado["Descripcion"]
        weakness = resultado["weakness"]
        resistances = resultado["resistances"]
        monstruo = Monstruo(name,weakness,resistances,descripcion)
        return monstruo