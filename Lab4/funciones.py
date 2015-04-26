import numpy as np 

def distanciaE(x,y): 
    #Considerando como puntos iniciales x1 = 0 e y1 = 0 
    x1 = 0 
    y1 = 0 
    difX = (x - x1)*(x - x1)
    difY = (y - y1)*(y - y1) 
    rep = np.sqrt(difX+difY) 
    return rep

    
