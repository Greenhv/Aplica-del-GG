from numpy import *
from sys import *
from cv2 import *
"""
Esta es la lista de todas aquellos parametros para cambiar de color una imagen.
flags = [i for i in dir() if i.startswith('COLOR_')]
print flags

Para gris : COLOR_BGR2GRAY
Para HSV : COLOR_BGR2HSV
"""

if len(argv)!=2:
	print "Incorrecta cantidad de argumentos"
else:
	img = imread(argv[1])
	if (img == None):
		print "No se puede abrir la imagen"
	else:			
		ret,thresh2 = threshold(img,127,255,THRESH_BINARY_INV)
		
		namedWindow('Display Window')
		imshow('Display Window',thresh2)
		waitKey(0)
		destroyAllWindows()
