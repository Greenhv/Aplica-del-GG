import sys
import funciones as fp
import numpy as np
import random as rm

def main():
    if (len(sys.argv)!=4):
        print("Ingrese la cantidad de argumentos (3)")
        return 0
    
    n=int(sys.argv[1])
    k=int(sys.argv[2])
    filename=sys.argv[3]
    print "correcto"
    f = open(filename,'r')
    L = []
    pivotes = []
    cluster = [[],[],[]]
    datosClus = []
    #Carga la matriz en una lista , cada elemento es una fila del archivo
    # de csv    
    for line in f:
        R = map(int,line[:-2].split(','))
        if len(R) > n:
            print "Se detecto un numero incorrecto de atributos"
            exit()
        L.append(R)
    #Calcula la posicion de los 3 pivotes dentro del arreglo L.
    for i in range(k):        
        pivotes.append(rm.randint(0,len(L)))    
    
    for i in range(len(L)):
        u = 0
        minima = fp.distanciaE(L[i],L[pivotes[0]])
        for j in range(1,k):
            dist = fp.distanciaE(L[i],L[pivotes[j]]) 
            if dist < minima:
                minima = dist
                u = j
        cluster[u].append(L[i])
        #L[i] = [0]*n 
   




    
if __name__=="__main__":
    main()
