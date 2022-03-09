import re

def PideNombre():
    nombre = input("Ingresa tu combre completo: ")
    while(validaNombre(nombre)):
        nombre = input("El texto ingresado no es un nombre válido, intentalo de nuevo: ")
    n = nombre
    return n

def validaNombre(nombre):
    #Busca todos los caracteres excepto letras de la A-Z o a-Z o espacios
    #Devuelve VERDADERO si encuentra algún caracter especial o número
    return re.search('[^a-zA-Z|\s]',nombre) 

def PideDireccion():
    direccion = input("Ingresa tu dirección: ")
    while(validaDireccion(direccion)):
        direccion = input("El texto ingresado no es una dirección válida, intentalo de nuevo: ")
    d = direccion
    return d

def validaDireccion(direccion):
    #Busca todos los caracteres que excepto letras de la A-Z o a-Z, números o espacios, 
    # incluye el simbolo #
    #Devuelve VERDADERO si encuentra algún caracter especial
    return re.search('[^a-zA-Z,\u0023,\s,\.,\d]',direccion)

def PideEdad():
    edad = input("Ingresa tu edad: ")
    while(not validaEdad(edad)):
        edad = input("El número ingresado no es una edad válida, intentalo de nuevo: ")
    e = edad
    return e

def validaEdad(edad):
    #Valida si es número y es entero
    return edad.isnumeric()

def PideCorreo():
    correo = input("Ingresa tu correo electrónico: ")
    while(not validaCorreo(correo)):
        correo = input("El texto ingresado no es una dirección email válida, intentalo de nuevo: ")
    c = correo
    return c

def validaCorreo(correo):
    #Valida correo electrónico del tipo mail@dominio.ter
    return re.fullmatch('[a-z0-9,\.]+\@{1}[a-z0-9,\.]+\.{1}[a-z]{2,3}',correo)

def PideTelefono():
    telefono = input("Ingresa tu número telefónico (formato: (+XX)XXXXXXXXXX): ")
    while(not validaTelefono(telefono)):
        telefono = input("El número ingresado no es un teléfono válido, intentalo de nuevo (ejemplo: (+52) 5545781425): ")

    t = {'Clave': re.search('(\({1}\+{1}\d{2}\){1})(\d{10})', telefono).group(1), 
        'Numero': re.search('(\({1}\+{1}\d{2}\){1})(\d{10})', telefono).group(2)}
    return t

def validaTelefono(telefono):
    #Valida número telefónico (+XX)XXXXXXXXXX
    return re.fullmatch('\({1}\+{1}\d{2}\){1}\d{10}',telefono)

_nombre = PideNombre()
_direccion = PideDireccion()
_edad = PideEdad()
_correo = PideCorreo()
_telefono = PideTelefono()

print(f'Resumen:\nNombre completo: {_nombre}\nDirección actual: {_direccion}\nEdad: {_edad}años\nEmail: {_correo}\nNúmero telefónico: {_telefono}')