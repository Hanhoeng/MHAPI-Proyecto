import pymongo
import MHConsulter as informer
from pymongo import MongoClient

def conectar(self):
    host = "localhost"
    port = 27017
    client = MongoClient(host,port)