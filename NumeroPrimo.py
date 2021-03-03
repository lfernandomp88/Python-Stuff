def esPrimo_if(numero):
  #Utilizo solo condicionales para evaluar primos, pero solo hasta los divisibles hasta 7
  if(numero%2==0):
    return "No es primo, divisible entre 2"
  elif(numero%3==0):
    return "No es primo, divisible entre 3"
  elif(numero%5==0):
    return "No es primo, divisible entre 5"
  elif(numero%7==0):
    return "No es primo, divisible entre 7"
  else:
    return "Es primo"
    
def esPrimo_for(numero):
  #Genera una expresión para todos los numeros hasta el numero elegido, si este es mayor que 1
  expr = (n for n in range(numero) if n > 1)
  #Utilizo un for con la expresión anterior
  for n in expr:
    #Si el residuo del numero entre n es 0
    if(numero%n==0):
      #No es primo
      return "No es primo, divisible entre ",n
  #Termino y regreso que no es primo
  return "Es primo"
    
print("11 ",esPrimo_if(11),"\n")
print("183 ",esPrimo_for(183),"\n")
print("221 ",esPrimo_if(221),"\n")
print("4149 ",esPrimo_for(4149),"\n")
print("9409 ",esPrimo_for(9409),"\n")
