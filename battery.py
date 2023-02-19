import os
from gtts import gTTS
from playsound import playsound
import re
import threading
import time


def mypass():
        #AQUI TAMBIEN PODEMOS OBTENER LA CONTRASEÑA DESDE UN ARCHICO CIFRADO O CON PERMISOS ESPECIFICOS
        mypass = 'YOUR TOKEN OR ROOT PASSSWORD'
        return mypass

def command(cmd):
        global text
        text = os.popen( "echo %s | sudo -S %s" % (mypass(),cmd) ).read()
        print(type(text))
        return text

def escribe_info ():
        with open("battery-data.txt", "w") as f:
                f.write((text))
        
def leer_informacion():
        global estado
        global porcentaje
        global natural
        file1 = open("battery-data.txt","r+") 
        print("Salida: ")
        #print(file1.readline())
        data = file1.readline()
        file1.close()
        print(data)
        li = list(data.split(" "))
        print(li)
        estado = li[2]
        print(estado)
        
        if estado == 'Charging,':
                estado = 'cargando'
        else:
                estado = 'descargando'
                porcentaje = li[3]
                natural = ([int(s) for s in re.findall(r'-?\d+\.?\d*', porcentaje)])
                print(porcentaje)
                print((natural))
        

def reproduce():
        s = gTTS(f'{estado}{porcentaje}', lang="es-us")
        s.save('sample.mp3')
        playsound('sample.mp3')

def timer():
    while True:
            
            
            (command('acpi -V'))
            escribe_info()
            leer_informacion()
            reproduce()
            print("Esperando . . ...")
            time.sleep(180)   # n segundos.

            
               
# Iniciar la ejecución en segundo plano.
t = threading.Thread(target=timer)
t.start()


