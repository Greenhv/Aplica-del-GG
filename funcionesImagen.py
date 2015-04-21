from cv2  import *
from numpy import *
import glob
import os


def lecturaEscrituraImagen(name):   
    img = imread(name,1)    
    #imwrite(img,'salida/'+name+'.png')
    return img


def testLecturaEscrituraImagen(name):
    #name = 'darthvader'        
    img =  lecturaEscrituraImagen(name)
    if(img==None):
        print('No hay imagen')
        return

    if not os.path.exists('salida'):
        os.makedirs('salida')
    imwrite('salida/'+name.split('.')[0]+'.png',img)        
    #imshow('DarthVader',img)    
    #waitKey(0)    
    

def modificacionPixeles(img):
    nuevo = 255 - img
    return nuevo

def testModificacionPixeles(nombre):
    imgIn = imread(nombre,1)
    imgOut = modificacionPixeles(imgIn)
    if not os.path.exists('salida'):
        os.makedirs('salida')
    imwrite('salida/ej2' + nombre.split('.')[0] + 'Inv.png',imgOut)


def espejarImagen(img):
    nuevo = img.copy()
    
    x,y = img.shape[:2]

    for i in range(x):
        z = y/2
        for j in range(z):			
            pix = nuevo[i][j].copy()
            nuevo[i][j] = nuevo[i][y-1-j].copy()
            nuevo[i][y-1-j] = pix

    #imwrite(nuevo,'salida/ej3'+name+'Espejo.png' )
    return nuevo

def testEspejoImagen(nombre):
    imgIn = imread(nombre,1)
    imgOut = espejarImagen(imgIn)
    if not os.path.exists('salida'):
        os.makedirs('salida')
    imwrite('salida/ej3'+nombre.split('.')[0]+'Espejo.png',imgOut)

def calcularHistograma(img, tipo):

    if(tipo=='GRAYSCALE'):
        L = []
        for i in range(256):
            L.append(0)    

        x,y = img.shape[:2]
        for i in range(x):
            for j in range(y):
                tonogris = int((img[i][j][0]*0.11 + img[i][j][1]*0.59 + img[i][j][2]*0.3))
                L[ tonogris ]+=1        
        return L
          
    elif(tipo=='RGB'):
        L = []
        for i in range(768):
            L.append(0)
        
        x,y = img.shape[:2]
        for i in range(x):
            for j in range(y):
                for k in range(3):
                    L[ (2-k)*256 + img[i][j][k] ]+=1                            
        return L
        # Detalle creo que la salida es BGR xD

def testHistogramaImagen(name,tipo):

	imgIn = imread(name,1)
	L = calcularHistograma(imgIn,tipo)

	print L

def caracterizarImagenes( carpeta, cad ):

    M = []    
    
    for name in glob.glob(carpeta+'/*.jpg'):     
        img = lecturaEscrituraImagen(name)    
        M.append( calcularHistograma(img,cad) )
        #M.append(carpeta)
    
        #print name

    if not os.path.exists('salida'):
        os.makedirs('salida')
    savetxt('salida/'+carpeta+'.csv', M,fmt='%d',delimiter=',' )


def testCaracterizarImagenes(name,tipo):
	caracterizarImagenes(name,tipo)

