from funcionesImagen import *

#name = raw_input('Ingrese el nombre de la imagen: ')

#tipo = raw_input('Ingrese GRAYSCALE o RGB:')

#testLecturaEscrituraImagen(name)

#testModificacionPixeles(name)

#testEspejoImagen(name)

#testHistogramaImagen(name,tipo)

while True:

    nombreCarpeta = raw_input('Ingrese el nombre de la carpeta: ')

    tipoImagen = raw_input('Ingrese GRAYSCALE o RGB:')
    
    testCaracterizarImagenes(nombreCarpeta,tipoImagen)
    
    door = raw_input('Existen mas carpetas? (Y/N): ')
    
    if door=='N':
        break
