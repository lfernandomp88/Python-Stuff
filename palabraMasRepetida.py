def palabraMasRepetida(frase):
  palabras = frase.split()
  contador = dict()
  mayor = ()

  for palabra in palabras:
    if(palabra in contador.keys()):
      contador[palabra]+=1
    else:
      contador[palabra]=1
  
  for item in contador.items():
    if(len(mayor)>0):
      if(item[1]  > mayor[1]):
        mayor = (item[0],item[1])
    else:
      mayor = (item[0],item[1])

  return mayor
  
print("La frase es: 'Both of these issues are fixed by postponing the evaluation of annotations. Instead of compiling code which executes expressions in annotations at their definition time, the compiler stores the annotation in a string form equivalent to the AST of the expression in question. If needed, annotations can be resolved at runtime using typing.get_type_hints(). In the common case where this is not required, the annotations are cheaper to store (since short strings are interned by the interpreter) and make startup time faster.")
print("\nLa palabra mas repetida es: ",palabraMasRepetida("Both of these issues are fixed by postponing the evaluation of annotations. Instead of compiling code which executes expressions in annotations at their definition time, the compiler stores the annotation in a string form equivalent to the AST of the expression in question. If needed, annotations can be resolved at runtime using typing.get_type_hints(). In the common case where this is not required, the annotations are cheaper to store (since short strings are interned by the interpreter) and make startup time faster."))
