import re

pensamiento = input("\nCuéntame algo: ")
# numPalabras = 0
# for palabra in pensamiento.split(' '):
#    numPalabras = numPalabras + 1

def cuentaPalabras(oracion):
    """Cuenta las palabras de una oración simple"""
    nPalabras = len(pensamiento.split(' '))
    return nPalabras

def cuentaPuntuacion(oracion):
    """Cuenta signos de puntuación"""
    #REGEX: Cadena con excepción de Espacios, Dígitos, Letras
    nSignos = len(re.findall('[^\s|\d|\w]',oracion))
    return nSignos

numPalabras = cuentaPalabras(pensamiento)
numSignos = cuentaPuntuacion(pensamiento)

print(f'Gracias por contarme en {numPalabras} palabras tus pensamientos, también encontré {numSignos} signos de puntuación.')