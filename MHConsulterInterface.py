from pymongo import MongoClient
from abc import ABC, abstractmethod
from Monster import Monstruo

# Entidades
## Monstruos
'''
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
'''
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
        resultado = self.col.find_one({"Nombre":nombre})
        #print(type(resultado))
        
        nombre = resultado["Nombre"]
        descripcion = resultado["Descripcion"]
        debilidades = resultado["Debilidades"]
        resistencias = resultado["Resistencias"]
        monstruo = Monstruo(nombre,debilidades,resistencias,descripcion)
        monstruo.setComentario(resultado["Comentario"])
        return monstruo
        

    def getMonsterByDebilidad(self, debilidad: str):
        monstruos=[]
        resultado = self.col.find({"Debilidades":debilidad})

        for i in resultado:
            nombre = i["Nombre"]
            debilidades = i["Debilidades"]
            resistencias = i["Resistencias"]
            descripcion = i["Descripcion"]
            comentario = i["Comentario"]
            monstruo = Monstruo(nombre,debilidades,resistencias,descripcion)
            monstruo.setComentario(comentario)
            monstruos.append(monstruo)
        return monstruos

    def getMonsterByResistencia(self, resistencia: str):
        resultado = self.col.find({"Resistencias":resistencia})
        monstruos=[]

        for i in resultado:
            nombre = i["Nombre"]
            debilidades = i["Debilidades"]
            resistencias = i["Resistencias"]
            descripcion = i["Descripcion"]
            comentario = i["Comentario"]
            monstruo = Monstruo(nombre,debilidades,resistencias,descripcion)
            monstruo.setComentario(comentario)
            monstruos.append(monstruo)
        return monstruos