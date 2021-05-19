import unittest
from unittest.mock import patch
from unittest.mock import patch, MagicMock
from MHRecorder import *
from MHConsulterInterface import *

class TestRequest(unittest.TestCase):

    def test_1(self):
        abrir = open ("data_prueba.txt",'w')
        d=MHRecorderGuardador().getRandomMonster()
        abrir.write(str(d))
        abrir.close()
        data_text2=open("data_prueba.txt","r")
        d1=data_text2.read()
        data_text2.close()
        clu=MHRecorderGuardador().getSavedMonstruos()
        self.assertNotEqual(str(clu), d1)

    def test_2(self):
        x1 = MHRecorderGuardador().getRMonster(6)
        x=MHRecorderGuardador().checkIfExist(x1)
        self.assertEqual(x,True)

    def test_3(self):
        x1 = MHRecorderGuardador().getRMonster(7)
        x=MHRecorderGuardador().checkIfExist(x1)
        self.assertEqual(x,False)

    def test_4(self):
        name="Apceros"
        d=MHConsulterBuscador().getMonsterByName(name)
        x=MHRecorderGuardador().checkIfExist(d)
        self.assertEqual(x, True)

    def test_5(self):#le dare una checada
        debilidad="fire"
        x=MHConsulterBuscador().getMonsterByDebilidad(debilidad)
        debilidad2="dragon"
        xp=MHConsulterBuscador().getMonsterByDebilidad(debilidad2)
        self.assertNotEqual(x, xp)

    def test_6(self):#le dare una checada
        a = open ("data_prueba.txt",'w')
        debilidad="fire"
        d=MHConsulterBuscador().getMonsterByDebilidad(debilidad)
        n=[]
        for i in d:
            n.append(i)
        a.write(str(d))
        a.close()
        data_text2=open("data_prueba.txt","r")
        d1=data_text2.read()
        data_text2.close()
        a = open ("data_prueba5.txt",'w')
        debilidad2="fire"
        xp=MHConsulterBuscador().getMonsterByDebilidad(debilidad2)
        m=[]
        for i in xp:
            m.append(i)
        a.write(str(xp))
        a.close()
        data_text5=open("data_prueba5.txt","r")
        d2=data_text5.read()
        data_text5.close()
        
        self.assertNotEqual(d1, d2)

    def test_7(self):#le dare una checada
        a = open ("data_prueba.txt",'w')
        debilidad="fire"
        d=MHConsulterBuscador().getMonsterByDebilidad(debilidad)
        n=[]
        for i in d:
            n.append(i)
        a.write(str(n))
        a.close()
        data_text2=open("data_prueba.txt","r")
        d1=data_text2.read()
        data_text2.close()
        a1 = open ("data_prueba5.txt",'w')
        debilidad2="dragon"
        xp=MHConsulterBuscador().getMonsterByDebilidad(debilidad2)
        m=[]
        for i in xp:
            m.append(i)
        a1.write(str(m))
        a1.close()
        data_text5=open("data_prueba5.txt","r")
        d2=data_text5.read()
        data_text5.close()
        self.assertNotEqual(d1, d2)

    @patch("Monster.Monstruo")
    def test_8(self,mock_response):
        mock_response=MHRecorderGuardador().getRMonster(26)
        self.assertEqual(MHRecorderGuardador().checkIfExist(mock_response),True)

    @patch("Monster.Monstruo")
    def test_9(self,mock_response):
        mock_response=MHRecorderGuardador().getRMonster(6)
        self.assertEqual(MHRecorderGuardador().checkIfExist(mock_response),True)

    @patch("Monster.Monstruo")
    def test_10(self,mock_response):
        mock_response=MHRecorderGuardador().getRMonster(1)
        self.assertEqual(MHRecorderGuardador().checkIfExist(mock_response),False)

    @patch("Monster.Monstruo")
    def test_11(self,mock_response):#Se revisara mañana jaja
        expected = [
            {"Nombre": "Shamos",
            "Debilidades":["fire","thunder"],
            "Resistencias":[],
            "Descripción":"Small nocturnal monsters. They're particularly vulnerable to Tzitzi-Ya-Ku's blinding flash, but have been known to gang up on enemies.",
            "Comentario":"Prueba de nuez"}
        ]        
        data_text35=open("prueba2.txt","r")
        d22=data_text35.read()
        data_text35.close()
        mock_response=MHConsulterBuscador().getMonsterByName("Shamos")
        print(mock_response)
        self.assertEqual(str(mock_response), d22)

if __name__ == "__main__":
    unittest.main()