import sys
import funciones as fp
import numpy as np
import random as rm

def main():
    if (len(sys.argv)!=4):
        print("Ingrese la cantidad de argumentos (3)")
        return 0
    
    n=sys.argv[1]
    k=sys.argv[2]
    filename=sys.argv[3]
    print "correcto"
    f = open(filename,'r')
    L = []
    #Carga la matriz en una lista , cada elemento es una fila del archivo
    # de csv    
    for line in f:
        R = line[0:len(line)-1].split(',')
        L.append(R)
    
    pivot1 = rm.randint(0,len(L))
    pivot2 = rm.randint(0,len(L))    
    pivot3 = rm.randint(0,len(L))
    
       
        
         
    
              
        




    
if __name__=="__main__" :
    main()
