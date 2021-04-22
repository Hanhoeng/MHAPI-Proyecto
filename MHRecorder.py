from abc import ABC, abstractmethod
from pymongo import MongoClient
import json
import requests
import random

# Entidades
## Monstruos
class Monstruo():
    def __init__(self, nombre:str,debilidades:list,resistencia:list,descripcion:str):
        self.nombre = nombre
        self.debilidades = debilidades
        self.resistencia = resistencia
        self.descripcion = descripcion

    def getNombre(self):
        return self.nombre
    def getDebilidad(self):
        return self.debilidades
    def getResistencia(self):
        return self.resistencia
    def getDescripcion(self):
        return self.descripcion

    def __str__(self) -> str:
        self.cadena = "Nombre: {}\n".format(self.nombre)
        self.cadena += "Debilidades: {}\n".format(self.debilidades)
        self.cadena += "resistencia: {}\n".format(self.resistencia)
        self.cadena += "descripción: {}\n".format(self.descripcion)
        return self.cadena
        
class MHRecorder(ABC):
    mongo_client = MongoClient(host="localhost",port=27017)
    db = mongo_client["MHConsulter"]
    col = db["Monster"]

    #listo
    @abstractmethod
    def setMonstruo(self, monstruo:Monstruo) -> bool:
        pass
    
    #listo
    @abstractmethod
    def checkIfExist(self, monstruo:Monstruo) -> bool:
        pass
    
    #listo
    @abstractmethod
    def getSavedMonstruos(self) -> list:
        pass

    #listo
    @abstractmethod
    def getRandomMonster(self) -> Monstruo:
        pass

class MHRecorderGuardador(MHRecorder):
    ### ATENCION AQUI: poner el puerto de tu base de mongo
    mongo_client = MongoClient(host="localhost",port=27017)
    db = mongo_client["MHConsulter"]
    col = db["Monster"]

    def getRandomMonster(self):
        id = random.randint(1,60)
        respuesta = requests.get("https://mhw-db.com/monsters/{}".format(id))
        respuesta = respuesta.text
        respuesta = json.loads(respuesta)
        #print(respuesta)
        nombre = respuesta["name"]
        debilidades = respuesta["weaknesses"]
        resistencias = respuesta["resistances"]
        descripcion = respuesta["description"]
        monstruo = Monstruo(nombre,debilidades,resistencias,descripcion)
        return monstruo

    def setMonstruo(self, monstruo: Monstruo):
        dicc = {
            "Nombre":Monstruo.getNombre(),
            "Debilidades":Monstruo.getDebilidad(),
            "Resistencias":Monstruo.getResistencia(),
            "Descripcion":Monstruo.getDescripcion()
        }

        documento = json.dumps(dicc)
        x = self.col.insert_one(dicc)
        if self.col.count_documents({"Nombre":monstruo.getNombre}, limit = 1) != 0:
            return True
        else:
            return False
        

    def checkIfExist(self, monstruo: Monstruo):
        nombre = monstruo.getNombre()
        if self.col.count_documents({ 'Nombre': nombre }, limit = 1) != 0:
            return True
        else:
            return False

    def getSavedMonstruos(self):
        monstruos = []
        for i in self.col.find({}):
            resultado = i
            monstruo = Monstruo(resultado["Nombre"],resultado["Debilidades"],resultado["Resistencias"],resultado["Descripcion"])
            monstruos.append(monstruo)

        for i in monstruos:
            print(i)