"""
Ya se poner comentarios de varias líneas! :)
"""

#Recorre e imprime el diccionario uno a uno
def recorrerDiccionario(diccionario):
  for indice, valor in diccionario.items():
    print("\n-",indice," le corresponde ",diccionario[indice])

#Recorre y suma los valores del diccionario  
def sumDiccionario(diccionario):
  suma = 0
  for indice, valor in diccionario.items():
    suma += int(diccionario[indice])
  print("\nLa suma es: ",suma)

#Hace un diccionario a partir de una lista  
def makeDiccionario(lista1,lista2):
  return dict(zip(lista1,lista2))

#Mezcla varios diccionarios en uno solo
def mixDiccionario(*dics):
  nuevoDic = dict()
  for dic in dics:
    for item in dic.keys():
      nuevoDic[item] = dic[item]
  return nuevoDic

dic = {'Manzana':15,'Pera':8,'Naranja':6,'Apio':7.5}
lista1 = ['Melon','Guayaba','Sandia','Manzana Verde']
lista2 = [25,32,27,30]
dic2 = dict()
print("\nPrimer diccionario: ",dic)
recorrerDiccionario(dic)
sumDiccionario(dic)
dic2 = makeDiccionario(lista1,lista2)
print("\nNuevo diccionario: ",dic2)
print("\nAñadiendo al anterior: ",mixDiccionario(dic,dic2))
sumDiccionario(mixDiccionario(dic,dic2))
    
