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
        a.write(str(n))
        a.close()
        data_text2=open("data_prueba.txt","r")
        d1=data_text2.read()
        data_text2.close()
        a = open ("data_prueba5.txt",'w')
        debilidad2="fire"
        xp=MHConsulterBuscador().getMonsterByDebilidad(debilidad2)
        m=[]
        for i in d:
            m.append(i)
        a.write(str(m))
        a.close()
        data_text5=open("data_prueba5.txt","r")
        d2=data_text5.read()
        data_text5.close()
        
        self.assertEqual(d1, d2)

if __name__ == "__main__":
    unittest.main()