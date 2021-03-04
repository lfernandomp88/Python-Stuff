import re

#Revisa mediante regEX si una cadena es válida como dirección IP de la forma:
#nnn.nnnn.nnn.nnn
#cada octeto debe estar entre 0 - 255 además de contemplar una cadena separada por '.'
#con un total de 4 octetos separados por un '.' cada uno.

def validaIP(direccion):
  print(direccion)
  validacion = re.findall("^((25[0-5]|(2[0-4]|1[0-9]|[1-9]|)[0-9])(\.(?!$)|$)){4}$",direccion)  #<- Aqui está la mágia!
  if(len(validacion)>0):
    return "Dirección válida"
  else:
    return "Dirección errónea"

print("Validador de direcciones IP\n")
print("Dirección: ")
print(validaIP("...1921681255"))
print("\n")
print("Dirección: ")
print(validaIP("192.168.1.256"))
print("\n")
print("Dirección: ")
print(validaIP("1.1.0.1"))
print("\n")
print("Dirección: ")
print(validaIP("255.255.255.0"))
print("\n")
