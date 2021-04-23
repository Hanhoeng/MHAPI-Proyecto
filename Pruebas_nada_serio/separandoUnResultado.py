from Pruebas_nada_serio.PruebasField import *
import json

'''
a y b se deben de arreglar porque esta raro, creo que igual no más llamando getAilment()
se arma el request
'''
a = 
b = getAilment("1")
#print(b)
'''
estuve experimentando con la API y esta rara la madre esta.
si haces el request sin id te da una tupla con todos los
ailments en un string que tiene una lista de diccionarios junto con el request 200...
si, te da una mamada de todo
así que el x,y=b divide la tupla; guarda lo que nos interesa en x y en y guarda el request 200, por ahora es basura
luego el objeto = json.loads(x) convierte el string en una lista de diccionarios
para ya acceder a un solo dato en concreto se toma como si fuera una matríz
eh ahí el porqué esta el print(objeto[0]['name']): el [0] le dice en que índice de la lista buscar y el
['name'] le dice la llave que debe de buscar en el diccionario que esta en el índice de la lista
espero ser suficientemente claro, alguna duda me preguntan chavos
'''
x, y = b
objeto = json.loads(x)
#print(objeto)
print(objeto['protection']['skills'][0]['name'])