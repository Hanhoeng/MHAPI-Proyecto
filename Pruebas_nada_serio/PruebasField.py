import json
import requests as peticiones
class coneccionAPIMH:
    mainURL="https://mhw-db.com/"
    localization=""
    busqueda=""
    id=""

    def setLocalization(self,localtag="en"):
        if localtag == "en":
            self.localization=""
        else:
            self.localization=localtag+"/"
    def getLocalization(self):
        return self.localization

    def setBusqueda(self,busqueda):
        self.busqueda=busqueda+"/"
    def getLocalization(self):
        return self.busqueda

    def setId(self,id=""):
        self.id=id
    def getId(self):
        return self.busqueda

    def ejecutorBusqueda(self):
        peticion = self.mainURL+self.localization+self.busqueda+self.id
        respuesta = peticiones.get(peticion)
        texto = respuesta.text
        return texto

    def transformTexto(respuestaplana:str):
        resTransformada = json.loads(respuestaplana)
        return resTransformada

if __name__ == '__main__':
    busqueda = coneccionAPIMH()
    busqueda.setLocalization()
    #print(busqueda.getLocalization())
    busqueda.setBusqueda("ailments")
    #print(busqueda.getLocalization())
    busqueda.setId("1")
    #resultado = busqueda.transformTexto()
    res = busqueda.ejecutorBusqueda()
    print(type(res))
    ahorasi = busqueda.transformTexto(res)
    print(ahorasi)
