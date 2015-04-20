from cv2  import *
from numpy import *


def lecturaEscrituraImagen(name):   
    img = imread(name+'.png',1)    
    #imwrite(img,'salida/'+name+'.png')
    return img


def testLecturaEscrituraImagen():
    name = 'darthvader'        
    img =  lecturaEscrituraImagen(name)
    if(img==None):
        print('No hay imagen')
        return
    imwrite('salida/'+name+'.png',img)        
    #imshow('DarthVader',img)    
    #waitKey(0)    
    

def modificacionPixeles(img):
    nuevo = img

    x,y = img.shape[:2]
    
    for i in x:
        for j in y:
            nuevo[i][j] = 255 - img[i][j]
    #imwrite(nuevo,'salida/ej2'+name+'Inv.png')
    return nuevo


def espejarImagen(img):
    nuevo = img
    
    x,y = img.shape[:2]

    for i in x:
        for j in y:
            nuevo[i][j] = img[i][y-1-j]        

    #imwrite(nuevo,'salida/ej3'+name+'Espejo.png' )
    return nuevo



def calcularHistograma(img, tipo):

    if(tipo=='GRAYSCALE'):
        L = []
        for i in range(256):
            L.append(0)    

        x,y = img.shape[:2]
        for i in x:
            for j in y:
                tonogris = (int)(img[i][j][0]*0.11 + img[i][j][1]*0.59 + img[i][j][2]*0.3)
                L[ tonogris ]+=1                            
        return L
          
    elif(tipo=='RGB'):
        L = []
        for i in range(768):
            L.append(0)
        
        x,y = img.shape[:2]
        for i in x:
            for j in y:
                for k in range(3):
                    L[ k*256 + img[i][j][0] ]+=1                            
        return L
        # Detalle creo que la salida es BGR xD

#Todo compila pero falta funciones test 


def caracterizarImagenes( carpeta, cad ):

    pos =1

    M = []    
    
    while(true):
        img = lecturaEscrituraImagen(carpeta+'/'+pos+'.png')   
        if(  img==None):
            break
        
        M.append( calcularHistograma(img,cad) )                              
        savetxt('salida/'+carpeta+'.csv', M )

        pos +=1


