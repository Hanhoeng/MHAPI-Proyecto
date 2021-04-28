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
        self.comentario = ""

    def getNombre(self):
        return self.nombre
    def getDebilidad(self):
        return self.debilidades
    def getResistencia(self):
        return self.resistencia
    def getDescripcion(self):
        return self.descripcion
    def getComentario(self):
        return self.comentario
    def setComentario(self, comentario):
        self.comentario = comentario

    def __str__(self) -> str:
        cadDebilidades = ""
        cadResistencias = ""
        for i in self.debilidades:
            cadDebilidades+="\t{}\n".format(i)

        for i in self.resistencia:
            cadResistencias += "\t{}\n".format(i)

        #print(cadDebilidades)

        self.cadena = "Nombre:\n\t{}\n".format(self.nombre)
        self.cadena += "Debilidades:\n{}".format(cadDebilidades)
        self.cadena += "Resistencias:\n{}".format(cadResistencias)
        self.cadena += "Descripción:\n\t{}\n".format(self.descripcion)
        self.cadena += "Comentario:\n\t{}\n".format(self.comentario)
        return self.cadena


        
class MHRecorder(ABC):

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
        debilidades = []
        for i in range(0,len(respuesta["weaknesses"])):
            debilidades.append(respuesta["weaknesses"][i]["element"])
        resistencias = []
        for i in range(0,len(respuesta["resistances"])):
            resistencias.append(respuesta["resistances"][i]["element"])
        descripcion = respuesta["description"]
        monstruo = Monstruo(nombre,debilidades,resistencias,descripcion)
        
        return monstruo

    def setMonstruo(self, monstruo: Monstruo):
        nombre = monstruo.getNombre()
        debilidades = monstruo.getDebilidad()
        resistencias = monstruo.getResistencia()
        descripcion = monstruo.getDescripcion()
        comentario = monstruo.getComentario()
        dicc = {
            "Nombre" : nombre,
            "Debilidades" : debilidades,
            "Resistencias" : resistencias,
            "Descripcion" : descripcion,
            "Comentario" : comentario
        }

        #documento = json.dumps(dicc)
        self.col.insert_one(dicc)
        if self.col.count_documents({"Nombre":monstruo.getNombre()}, limit = 1) != 0:
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
            nombre = i["Nombre"]
            debilidades = i["Debilidades"]
            resistencias = i["Resistencias"]
            descripcion = i["Descripcion"]
            monstruo = Monstruo(nombre,debilidades,resistencias,descripcion)
            monstruo.setComentario(i["Comentario"])
            monstruos.append(monstruo)
        return monstruos