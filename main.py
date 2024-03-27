import cv2
import numpy as np
import face_recognition as fr
import os
import random
from datetime import datetime


#Se accede a la carpeta
path= 'personal'
images=[]
clases=[]
lista= os.listdir(path)

#Variables
comp1=100

#Leer el rostro en la carpeta
for lis in lista:
    imagdb=cv2.imread(f'{path}/{lis}')
    images.append(imagdb)
    clases.append(os.path.splitext(lis)[0])

print(clases)

#Codificar los rostros
def codrostros(images):
    listacod=[]
    for img in images:
        img= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        cod= fr.face_encodings(img)[0]
        listacod.append(cod)

    return listacod

def horario(nombre):
    #Abrir el archivo en modo de lectura y escritura
    with open('Horario.csv','r+') as h:
        #Leemos la información
        data=h.readline()
        listanombres=[]
        for line in data:
            #Se busca la entrada y se la diferencia con ,
            entrada = line.split(',')
            listanombres.append(entrada[0])

        if nombre not in listanombres:
            #Se extrae la información actual
            info= datetime.now()
            #Se extrae la fecha
            fecha=info.strftime('%Y:%m:%d')
            #Se extrae la hora
            hora= info.strftime('%H:%M:%S')

            #Se guarda la información
            h.writelines(f'\n{nombre},{fecha},{hora}')
            print(info)
def run():
    # Llamada a la funci[on
    rostroscod = codrostros(images)

    # VideoCaptura
    cap = cv2.VideoCapture(0)
    # bandera=kb.Listener(pulsa, suelta).run()

    while True:
        # Se lee las fotografias
        ret, frame = cap.read()
        t = cv2.waitKey(1)

        # Se reduce las imagenes para mejor procesamiento
        frame2 = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
        rgb = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB)

        # Busqueda de rostros
        faces = fr.face_locations(rgb)
        facescod = fr.face_encodings(rgb, faces)

        for facecod, faceloc in zip(facescod, faces):
            # Se compara el rostro de la DB con el de tiempo real
            comparacion = fr.compare_faces(rostroscod, facecod)

            # Se calcula la similitud
            simi = fr.face_distance(rostroscod, facecod)
            # Busca el valor m[as bajo
            min = np.argmin(simi)
            print(min)

            if comparacion[min]:
                nombre = clases[min].upper()
                print(nombre)

                # Se extraen las coordenadas
                yi, xf, yf, xi = faceloc
                yi, xf, yf, xi = yi * 4, xf * 4, yf * 4, xi * 4

                indice = comparacion.index(True)
                global comp1
                if comp1 != indice:
                    r = random.randrange(0, 255, 50)
                    g = random.randrange(0, 255, 50)
                    b = random.randrange(0, 255, 50)
                    comp1 = indice

                if comp1 == indice:
                    cv2.rectangle(frame, (xi, yi), (xf + 50, yf + 5), (r, g, b), 3)
                    cv2.rectangle(frame, (xi, yf - 35), (xf + 50, yf), (r, g, b), cv2.FILLED)
                    cv2.putText(frame, nombre, (xi + 20, yf - 6), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                    if (t == 13):
                        horario(nombre)

        cv2.imshow("Reconocimiento facial", frame)
        # kb.Listener(pulsa, suelta).run()
        # Lectura de teclado

        if t == 27:
            break
    cv2.destroyAllWindows()
    cap.release()

