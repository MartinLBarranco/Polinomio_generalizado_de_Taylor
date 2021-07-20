# Polinomio_generalizado_de_Taylor

Es necesario que antes de empezar a trabajar, se importe la librería sympy (poner "from sympy import * ") y declarar una variable simbólica (declarar la variable x = symbols("x")).

Las funcionciones son las siguientes:

**getLatexAPI(s, conjunto, clase, mathmode=false,showname=true)**
Donde s es una string que contiene la expresión de la función. Conjunto son los puntos donde se halla el polinómio. Clase es las veces que puede derivarse. mathmode mete el string resultante entre $s. Showname incluye "P_\{f,conjunto, clase} = " 

**getPythonExpressionAPI(s,conjunto,clase)**
devuelve la expresion del polinomio en sintaxis de sympy, s es la expresion de la funcion como string

**getPolListAPI(s,conjunto,clase)**
Devuelva la lista de los coeficientes del polinomio generalizado. s vuelve a ser un string


Para evaluar un polinomio en un punto, usar el metodo .subs(x,x_0) donde x_0 es el valor que queremos poner, x es la variable simbólica que hemos iniciado al principio.
