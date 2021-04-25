from re import X

from pymongo.encryption import _MONGOCRYPTD_TIMEOUT_MS
from MHRecorder import MHRecorderGuardador
from MHConsulterInterface import MHConsulterBuscador

print("Bienvenido a MHConsulter.\n\nQue desea hacer?\n\n1.- Dame un monstruo al azar.\n2.- Dame todos los monstruos encontrados.\n3.- Buscar un monstruo.")
eleccion0 = input()

if eleccion0=="1":
    x = MHRecorderGuardador().getRandomMonster()
    print(x)
    eleccion1 = input("Desea guardar el monstruo? (y/n): ")

    if eleccion1=="y":
        respuesta = MHRecorderGuardador().checkIfExist(x)
        if respuesta:
            print("Este monstruo ya se encontro.")
        else:
            print("Este monstruo aun no se encuentra.")
            eleccion2 = input("Desea registrarlo?(y/n): ")
            if eleccion2=="y":
                comentario = input("Antes de guardar, agregue un comentario:  ")
                x.setComentario(comentario)
                if MHRecorderGuardador().setMonstruo(x):
                    print("Se guardo con exito!!!")
                else:
                    print("Algo fallo!!!")
            else:
                print("Hasta pronto.")
    else:
        print("Hasta pronto")
        pass
elif eleccion0=="2":
    resultado = MHRecorderGuardador().getSavedMonstruos()
elif eleccion0=="3":
    eleccion4 = input("Por que quieres buscar...?\n1.- Por nombre.\n2.- Por Debilidad.\n3.- Por Resistencia.\n")
    if eleccion4=="1":
        nombreM = input("Dame el nombre: ")
        monstruo = MHConsulterBuscador().getMonsterByName(nombreM)
        print(monstruo)
    elif eleccion4=="2":
        debilidadM = input("Dame la debilidad: ")
        monstruo = MHConsulterBuscador().getMonsterByDebilidad(debilidadM)
        for i in monstruo:
            print(i)
    elif eleccion4=="3":
        resistenciaM = input("Dame la resistenca: ")
        monstruo = MHConsulterBuscador().getMonsterByResistencia(resistenciaM)
        for i in monstruo:
            print(i)