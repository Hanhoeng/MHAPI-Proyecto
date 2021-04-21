import json
import requests as peticion

class MHConsulter():
    URL="https://mhw-db.com/"
    item=""
    id=""
    strpeticion=""
    respuestaPlana=""
    respuestaTransformada=""

    def setItemAilments(self):
        self.item="ailments/"
    def setAilmentId(self,id:str):
        self.id=id

    def setItemArmor(self):
        self.item="armor/"
    def setArmorId(self,id:str):
        self.id=id

    def setItemArmorSets(self):
        self.item="armor/sets/"
    def setArmorSetId(self,id:str):
        self.id=id

    def setItemCharms(self):
        self.item="charms/"
    def setCharmId(self,id:str):
        self.id=id

    def setItemDecorations(self):
        self.item="decorations/"
    def setDecorationId(self,id:str):
        self.id=id
    
    def setItemEvents(self):
        self.item="events/"
    def setEventId(self,id:str):
        self.id=id

    def setItemItems(self):
        self.item="items/"
    def setItemsId(self,id:str):
        self.id=id
    
    def setItemLocations(self):
        self.item="locations/"
    def setLocationsId(self,id:str):
        self.id=id

    def setItemMonsters(self):
        self.item="monsters/"
    def setMonstersId(self,id:str):
        self.id=id

    def setItemMotionValues(self):
        self.item="motion-values/"
    def setMotionValueId(self,id:str):
        self.id=id

    def setItemSkills(self):
        self.item="skills/"
    def setItemSkillsId(self,id:str):
        self.id=id

    def setItemWeapons(self):
        self.item="weapons/"
    def setWeaponId(self,id:str):
        self.id=id

    def construirPeticion(self):
        self.strpeticion=self.URL+self.item+self.id
    def getPeticionConstruida(self):
        return self.strpeticion

    def ejecutarPeticion(self):
        self.respuestaPlana = peticion.get(self.strpeticion)
    def getRespuestaPlana(self):
        return self.respuestaPlana

    def transformText(self):
        texto = (self.respuestaPlana).text
        self.respuestaTransformada=json.loads(texto)
    def getRespuestaTransformada(self):
        return self.respuestaTransformada

    def serializationJson(self):
        json_object=json.dumps(self.respuestaTransformada,indent=1)
        return json_object


if __name__ == "__main__":
    resultado = MHConsulter()
    resultado.setItemAilments()
    resultado.setAilmentId("1")

    resultado.construirPeticion()
    #print(resultado.getPeticionConstruida())
    #print(type(resultado.getPeticionConstruida()))
    #print("")
    
    resultado.ejecutarPeticion()
    #print(resultado.getRespuestaPlana())
    #print(type(resultado.getRespuestaPlana()))
    #print("")

    resultado.transformText()
    #print(resultado.getRespuestaTransformada())
    #print(type(resultado.getRespuestaTransformada()))
    #print("")
    print(resultado.serializationJson())
    #print(type(resultado.serializationJson()))