**Documentación de la API:**

Es necesario que antes de empezar a trabajar, se importe la librería sympy (poner "from sympy import * ") y declarar una variable simbólica (declarar la variable x = symbols("x")). Es decir, hay que poner esto antes de empezar:


```
from sympy import *

x = symbols("x")
```



Las funcionciones son las siguientes:

**getLatexAPI(s, conjunto, clase, mathmode=false,showname=true)**
Donde s es una string que contiene la expresión de la función. Conjunto son los puntos donde se halla el polinómio. Clase es las veces que puede derivarse. mathmode mete el string resultante entre $s. Showname incluye "P_\{f,conjunto, clase} = " 

**getPythonExpressionAPI(s,conjunto,clase)**
devuelve la expresion del polinomio en sintaxis de sympy, s es la expresion de la funcion como string

**getPolListAPI(s,conjunto,clase)**
Devuelva la lista de los coeficientes del polinomio generalizado. s vuelve a ser un string

Veamos un ejemplo de uso:



```
from sympy import *

x = symbols("x")

s = "sin(x) + exp(x-7)"
polinomio = getLatexAPI(s, 3, true, false)
print(polinomio)
```

Esto imprimirá en consola:

```
$P_{exp(x - 7) + sin(x),[0, 1],True} = \frac{- 2 e^{7} \sin{\left(1 \right)} - e + 3 + e^{7} \cos{\left(1 \right)} + e^{7}}{e^{7}} x^{3} + \frac{- 2 e^{7} - e^{7} \cos{\left(1 \right)} - 5 + 2 e + 3 e^{7} \sin{\left(1 \right)}}{e^{7}} x^{2} + \frac{1 + e^{7}}{e^{7}} x + e^{-7}$
```


La complejidad computacional no está calculada, ni tengo intentción de hacerlo. Pero va como la seda, confía en mi :)
