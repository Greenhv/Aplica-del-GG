import numpy as np 

def distanciaE(X,Y): 
    # Es una distancia euclidiana en N dimensiones     
    n = len(X)
    rep=0.0
    for i in range(n):
        rep += (Y[i]-X[i])*(Y[i]-X[i]) 
    rep = np.sqrt(rep) 
    return rep




def asignar( X, R ):
    # de cual de todos lo pivotes dista menos
    k= len(R)
    ans = -1;
    dist = -1;
    for i in range(k):
        act = distanciaE( X , R[i] )
        if( dist<0 or dist>act  ):
            dist=act
            ans = i
    return ans
    



def centroides(flag, M,antR):
    # reasignamos pivotes a centroides
    k = len(antR)
    cant = len(M)
    n = len(M[0])    
    R = []
    num=[]
    for i in range(k):
        R.append([])
        for j in range(n):    
            R[i].append(0.0)
        num.append(0.0)

    R = np.array(R)    
    for i in range(cant):
        R[ flag[i] ] = np.add( R[flag[i] ],M[i])
        #print R
        num[flag[i]]+=1    

    
    for i in range(k):
        if num[i]==0:
            R[i] = 1.0*antR[i]
        else:    
            R[i]  = R[i]*1.0/num[i]      
    return R



