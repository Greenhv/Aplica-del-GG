from numpy import *
from sys import *
from cv2 import *

#Para mas información visiten : http://www.weheartcv.com/understanding-image/
# Hay problemas interesantes para hacer y aprender :D 
img = imread('yoda.png',0)

dts = flip(img,1)
#0 -> Rows , 1 -> Colums
print img.shape[0]
print img.shape[1]
imshow('lol',dts)
waitKey(0)
destroyAllWindows()

