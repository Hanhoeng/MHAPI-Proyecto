import pymongo
import json
from pymongo import MongoClient
from MHConsulter import *

client = MongoClient("localhost", 27017)
db = client["mi-db"]
# Obtén un registro
print("Imprime un registro\n", db.Monster.find_one(), "\n")

# Obtén todos los registros
print("Imprime todos los registros")
#for Monster in db.Monster.find():
print("Mete el jodido monstruo")
monsB=input()
query= {
    "name": monsB}
print(query)
doc= db.Monster.find(query)
print(doc)
for x in doc:
    print(x)
