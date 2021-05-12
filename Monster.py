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
