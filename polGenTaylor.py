from sympy import *
from sympy.matrices import Matrix

#CODIGO PARA CREAR LOS VECTORES Y LAS MATRICES
#Esto crea las filas de las matrices A_i
def creaVectorDeMatriz(grado,punto,vecesDeriva):
  x = symbols("x")                                              #Creo la variable con la que trabajamos
  lista = [diff(x**j, x, vecesDeriva) for j in range(grado+1)]  #Crea la fila 
  v = [lista[j].subs(x,punto) for j in range(grado+1)]          #Se sustituye cada punto
  return v


#Funcion para crear las matrices A_i
def creaMatrizI(grado, conjunto, vecesDeriva):
  listas_filas = [creaVectorDeMatriz(grado,punto,vecesDeriva) for punto in conjunto]   #Es una lista cuyos elementos (listas también) son los vectores
  matriz = Matrix(listas_filas)                                                        #pasa la lista de lista a una matriz
  return matriz


#Esto hace la matriz de todo el sistema
def superMatriz(grado, conjunto, clase):
  M = Matrix()                        #Creamos la matriz que será la supermatriz
  for j in range(clase+1):            #Vamos creando las A_i y las vamos concatenando verticalmente a M
    m = creaMatrizI(grado,conjunto,j) #Crea la matriz A_i
    M = Matrix.vstack(M,m)            #Se pega debajo de M (supermatriz)
  return M


#HALLAR EL VECTOR SOLUCIÓN
#La variable de fun debe ser nombrada como x. Esta funcion crea la parte del vector asociada a cada derivada i-esima.
def solI(fun, conjunto, vecesDeriva):
  fun_sol = diff(fun, x, vecesDeriva)                 #Deriva la funcion i veces
  k = [fun_sol.subs(x, punto) for punto in conjunto]  # crea la lista de el valor de la funcion i veces derivada en cada punto.
  return Matrix(k)                                    #Matrix() convierte una lista en una matriz, en este caso un vector.


#Esto crea todo el vector. Concatena en el orden correcto los minivectores sacados de solI() ordenados de menor a mayor verticalmente,
def solucion(fun,conjunto,clase):
  sol = Matrix()                  #Se crea el vector que será la solucion
  for j in range(clase+1):
    v = solI(fun,conjunto,j)      #Se crea el trozo nuevo de la solucion
    sol = Matrix.vstack(sol,v)    #Se concatena el nuevo vector al vector solucion
  return sol


#HALLA EL POLINOMIO DÁNDOSELE UNA FUNCIÓN, EL CONJUNTO Y LA CLASE.
def hallaPol(fun, conjunto, clase):
  if clase <0 or len(conjunto) == 0:
    raise Exception("Has puesto números erróneos.")
  elif clase == 0:
    raise Exception("Se trata de un problema de interpolación polinómica")
  elif len(conjunto) == 1:
    raise Exception("Se trata del polinomio de Taylor")
  else:
    conjunto = sorted(conjunto)
    deg = len(conjunto)*(clase + 1) -1      #Usando el teorema, se halla el grado del poliomio.
    A = superMatriz(deg, conjunto, clase)   #Creamos la supermatriz de coeficiente.
    b = solucion(fun, conjunto, clase)      #Creaos el vector solución
    terminos = linsolve((A,b))              #Usamos esta funcion de sympy para resolver el sistema de ecuaciones lineales. Es una "tupla especial" de sympy
    terminos = list(terminos)               #Lo convertimos en lista por que de otra forma peta y no se arreglarlo
    lista = []                              #Aquí se pondrán los coeficientes del polinomio  
    for elem in terminos[0]:                #Metemos en la lista los elementos en orden inverso, ya que linsolve los devuelve en orden inverso
      lista.insert(0,elem)
    x = symbols("x")
    return Poly.from_list(lista, x)         #Hacemos un polinomio a traves de la lista usando x como variable


#Lo mismo que la funcion anterior pero devuelve la lista de los coeficientes.
def hallaPolLista(fun, conjunto, clase):
  if clase <0 or len(conjunto) == 0:
    raise Exception("Has puesto números erróneos.")
  elif clase == 0:
    raise Exception("Se trata de un problema de interpolación polinómica")
  elif len(conjunto) == 1:
    raise Exception("Se trata del polinomio de Taylor")
  else:
    conjunto = sorted(conjunto)
    deg = len(conjunto)*(clase + 1) -1      #Usando el teorema, se halla el grado del poliomio.
    A = superMatriz(deg, conjunto, clase)   #Creamos la supermatriz de coeficiente.
    b = solucion(fun, conjunto, clase)      #Creaos el vector solución
    terminos = linsolve((A,b))              #Usamos esta funcion de sympy para resolver el sistema de ecuaciones lineales. Es una "tupla especial" de sympy
    terminos = list(terminos)               #Lo convertimos en lista por que de otra forma peta y no se arreglarlo
    lista = []                              #Aquí se pondrán los coeficientes del polinomio  
    for elem in terminos[0]:                #Metemos en la lista los elementos en orden inverso, ya que linsolve los devuelve en orden inverso
      lista.insert(0,elem)
    return lista


def getLatex(fun, conjunto, clase, mathmode=false,showname=true):
  poli = hallaPol(fun, conjunto, clase)                   #Hallamos el polinomio
  expre = latex(poli)                                     #Lo pasamos a Latex
  inicio_expre = expre[27::]                              # Le quita las chorradas de alante al latex
  inicio_expre = inicio_expre[::-1]                       #Le damos la vuelta
  indice_x = inicio_expre.index("x")                      #Encontramos donde esta la x por la que hay que truncar
  expre = inicio_expre[indice_x+3:]                       #Truncamos por donde está la x
  final = expre[::-1]                                     #Volvemos a dar la vuelta
  if showname:                                            #Si showname es true, ponemos P_{f,I,k}
    extra = "P_{" + str(fun)+ "," + str(conjunto) + "," + str(clase) + "} = "   #Creamos el trocito del nombre del polinomio
    final = extra + final                                 #Pegamos ambos strings
  if mathmode:                                            #Si mathmode es true ponemos la expresion entre "$"
    final = "$" + final + "$"
  return final
def getLatexAPI(s, conjunto, clase, mathmode=false,showname=true):
  fun = parse_expr(s)
  res = getLatex(fun,conjunto,clase,mathmode,showname)
  return res

def getPythonExpressionAPI(s,conjunto,clase):
  fun = parse_expr(s)
  f = hallaPol(fun, conjunto, clase)
  res = str(f)
  res = res[5:]
  res = res[::-1]
  indice_x = res.index("x")    
  res = res[indice_x+3:]
  res = res[::-1]
  ex = parse_expr(res)            
  return ex

def getPolListAPI(s,conjunto,clase):
  fun = parse_expr(s)
  res = hallaPolLista(fun,conjunto,clase)
  return res
