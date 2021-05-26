import mock
from mock import Mock
from pymongo import MongoClient
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

    def test_5(self):
        debilidad="fire"
        x=MHConsulterBuscador().getMonsterByDebilidad(debilidad)
        debilidad2="dragon"
        xp=MHConsulterBuscador().getMonsterByDebilidad(debilidad2)
        self.assertNotEqual(x, xp)

    def test_6(self):
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

    def test_7(self):
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
    def test_11(self,mock_response):
        expected = "Nombre:\n\tShamos\nDebilidades:\n\tfire\n\tthunder\nResistencias:\nDescripción:\n\tSmall nocturnal monsters. They're particularly vulnerable to Tzitzi-Ya-Ku's blinding flash, but have been known to gang up on enemies.\nComentario:\n\tPrueba de nuez"
        mock_response=str(MHConsulterBuscador().getMonsterByName("Shamos"))
        self.assertEqual(mock_response, expected)

    @patch("Monster.Monstruo")
    def test_12(self,mock_response):
        expected = "Nombre:\n\tShamos\nDebilidades:\n\tfire\n\tthunder\nResistencias:\nDescripción:\n\tSmall nocturnal monsters. They're particularly vulnerable to Tzitzi-Ya-Ku's blinding flash, but have been known to gang up on enemies.\nComentario:\n\tPrueba de nuez"
        mock_response=str(MHConsulterBuscador().getMonsterByName("Behemoth"))
        self.assertNotEqual(mock_response, expected)

    @mock.patch("pymongo.mongo_client.MongoClient")
    def test_13(self,mock_method):
        result=('localhost', 27017)
        mock_method =MHConsulterBuscador().mongo_client.address
        self.assertEqual(mock_method, result)

    @mock.patch("pymongo.mongo_client.MongoClient")
    def test_14(self,mock_method):
        result=('Mongo', 00000)
        mock_method =MHConsulterBuscador().mongo_client.address
        self.assertNotEqual(mock_method, result)
    
    @mock.patch("pymongo.mongo_client.MongoClient")
    def test_15(self,mock_method):
        result="MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True)"
        mock_method = str(MHConsulterBuscador().mongo_client)
        self.assertEqual(mock_method, result)

    @mock.patch("MHConsulterInterface.MHConsulterBuscador.getMonsterByName")
    def test_16(self,mock_response):
        debilidad16 = "fire"
        mock_response = MagicMock()
        mock_response = MHConsulterBuscador().getMonsterByDebilidad(debilidad16)
        actual =   MHRecorderGuardador().checkIfExist(mock_response[0])
        self.assertEqual(actual, True)

    @mock.patch("MHConsulterInterface.MHConsulterBuscador.getMonsterByResistencia")
    def test_17(self,mock_response):
        debilidad17 = "fire"
        mock_response.getMonsterByResistencia.return_value= []
        das= mock_response.getMonsterByResistencia(debilidad17) 
           
        self.assertEqual(das, [])

    

if __name__ == "__main__":
    unittest.main()