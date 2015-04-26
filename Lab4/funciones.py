import numpy as np 

def distanciaE(pos1,posPiv):      
    difX = (posPiv[0] - pos1[0])*(posPiv[0] - pos1[0])
    difY = (posPiv[1] - pos1[1])*(posPiv[1] - pos1[1])
    rep = np.sqrt(difX+difY) 
    return rep

    
