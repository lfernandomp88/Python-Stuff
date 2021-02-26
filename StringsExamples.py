def palabraMasRepetida(frase):
  palabras = frase.split()
  contador = dict()
  mayor = ()

  #Armar diccionario de palabras, con las veces que se ha usado cada palabra.
  for palabra in palabras:
    if(palabra in contador.keys()):
      contador[palabra]+=1
    else:
      contador[palabra]=1
  
  #Recorremos el diccionario y vamos viendo cual es la que más se repite.
  for item in contador.items():
    if(len(mayor)>0): #Si el diccionario NO está vacio
      if(item[1]  > mayor[1]): #Si las veces que se ha usado la palabra actual es mayor que la última.
        mayor = (item[0],item[1]) #Ahora la mayor es la última.
    else:
      mayor = (item[0],item[1]) #La mayor es la actual.

  return mayor
  
print("La frase es: 'Both of these issues are fixed by postponing the evaluation of annotations. Instead of compiling code which executes expressions in annotations at their definition time, the compiler stores the annotation in a string form equivalent to the AST of the expression in question. If needed, annotations can be resolved at runtime using typing.get_type_hints(). In the common case where this is not required, the annotations are cheaper to store (since short strings are interned by the interpreter) and make startup time faster.")
print("\nLa palabra mas repetida es: ",palabraMasRepetida("Both of these issues are fixed by postponing the evaluation of annotations. Instead of compiling code which executes expressions in annotations at their definition time, the compiler stores the annotation in a string form equivalent to the AST of the expression in question. If needed, annotations can be resolved at runtime using typing.get_type_hints(). In the common case where this is not required, the annotations are cheaper to store (since short strings are interned by the interpreter) and make startup time faster."))
