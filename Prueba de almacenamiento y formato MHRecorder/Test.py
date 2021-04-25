import unittest
from unittest.mock import patch
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
        print(type(d))
        x=MHRecorderGuardador().checkIfExist(d)
        self.assertEqual(x, True)

    def test_5(self):
        debilidad="fire"
        x=MHConsulterBuscador().getMonsterByDebilidad(debilidad)
        print(type(x))
        d=("data_prueba.txt", "w")
        self.assertEqual(x, True)

if __name__ == "__main__":
    unittest.main()