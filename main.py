from re import X
from MHRecorder import MHRecorder, MHRecorderGuardador
import MHConsulterInterface

print("Bienvenido a MHConsulter\n\nQue desea hacer?\n\n1.- Dame un monstruo al azar\n2.- Dame todos los monstruos encontrados")
eleccion0 = input()
if eleccion0=="1":
    x = MHRecorderGuardador().getRandomMonster()
    print(x)
    eleccion1 = input("Desea guardar el monstruo? (y/n)")

    if eleccion1=="y":
        respuesta = MHRecorderGuardador().checkIfExist(x)
        if respuesta:
            print("Este monstruo ya encontro")
        else:
            print("Este monstruo aun no se encuentra")
    else:
        print("Weno :B chaito pues")

    eleccion2 = input("Desea registrarlo?(y/n)")
    
    if eleccion2=="y":
        comentario = input("Antes de guardar, agrefue un comentario :D")
        x.setComentario(comentario)
        if MHRecorderGuardador().setMonstruo(x):
            print("Se guardo con exito :D")
        else:
            print("Algo fallo :c")
    else:
        print("Weno :B Chaito pues")
elif eleccion0=="2":
    resultado = MHRecorderGuardador().getSavedMonstruos()