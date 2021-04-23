from pymongo import MongoClient

mongo_client = MongoClient(host="localhost",port=27017)
db = mongo_client["MHConsulter"]
col = db["Monster"]

resultados = col.find({"Debilidades":"fire"})

for i in resultados:
    print(i["Nombre"])