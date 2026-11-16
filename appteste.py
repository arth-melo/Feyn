from script import copiar
from consultaApi import consulta
from testeinterface import interface
import keyboard as ky
def pipeline():
    print("carregando...")
    texto = copiar()
    info = consulta(texto)
    interface(info)
ky.add_hotkey('alt+a', pipeline, suppress=True)
ky.wait()


	
