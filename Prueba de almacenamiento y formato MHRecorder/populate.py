import pymongo
import json
from pymongo import MongoClient
from MHConsulter import *

client = MongoClient("localhost", 27017)
db = client["mi-db"]
print ("version:", pymongo.version)
# Name
print("Nombre de la DB: ", db.name)
print(client.list_database_names())

resultado = MHConsulter()
resultado.setItemMonsters()
resultado.setMonstersId("1")
resultado.construirPeticion()
resultado.ejecutarPeticion()
resultado.transformText()

#prueba = 
#prueba = json.dump(prueba)
prueba2 = json.loads(resultado.serializationJson())
print(prueba2)
Id= prueba2["id"]
name = prueba2["name"]
des = prueba2["description"]
com = input()
#re=prueba2["recovery"]
#ro=json.dumps(re)
#print(ro)
print(Id)
print(name)
print("locations")
re=""
ro=""
for el in prueba2["locations"]:
    re+=el["name"]+" "
for el in prueba2["weaknesses"]:
    ro+=el["element"]+" "
# Crea colección e inserta un registro
print(db.Monster.insert_one({
        "_id": Id,
        "name": name,
        "Descripcion": des,
        "Comentario": com,
        "locations": re,
        "weaknesses": ro
    }))