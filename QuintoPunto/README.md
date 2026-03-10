# Punto 5 – Aproximación de (e^x) usando la Serie de Maclaurin con ANTLR

## Descripción

En este punto se implementó un programa que utiliza **ANTLR** para reconocer una expresión de entrada y calcular una aproximación del valor de (e^x) utilizando la **serie de Maclaurin**.

La entrada del programa tiene el formato:

```
exp(x,n)
```

donde:

* **x** representa el valor al que se desea evaluar la función exponencial.
* **n** representa el número de términos que se utilizarán en la serie.

---

## Serie de Maclaurin

La función exponencial puede aproximarse mediante la siguiente serie infinita:

[
e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!}
]

En el programa se utiliza una **aproximación truncada**, es decir, se calculan únicamente los **primeros n términos de la serie**.

Esto permite obtener una aproximación del valor de (e^x).

---

## Ejemplo de entrada

Archivo `entrada.txt`:

```
exp(1,10)
```

Esto indica que se calculará la aproximación de (e^1) utilizando **10 términos de la serie**.

---

## Resultado obtenido

Al ejecutar el programa se obtuvo el siguiente resultado:

```
Aproximacion de e^x:
2.7182815255731922
```

El valor real del número de Euler es:

[
e = 2.718281828459045
]

Como se puede observar, la aproximación obtenida es **muy cercana al valor real**, lo que demuestra que la serie de Maclaurin permite calcular correctamente el valor de la función exponencial utilizando un número limitado de términos.

---

## Archivos del punto

Este punto está compuesto por los siguientes archivos:

* `Maclaurin.g4` → Gramática utilizada por ANTLR.
* `Main.java` → Programa principal que calcula la serie.
* `entrada.txt` → Archivo con la expresión de entrada.

---

## Comandos utilizados

Para generar el analizador y ejecutar el programa se utilizaron los siguientes comandos:

```
antlr4 Maclaurin.g4
javac *.java
java Main
```

---

## Conclusión

El uso de **ANTLR** permite definir una gramática para reconocer una expresión de entrada y posteriormente procesarla en un programa.

En este caso, se utilizó para interpretar una expresión que representa el cálculo de (e^x) y aplicar la **serie de Maclaurin**, obteniendo una aproximación numérica precisa del valor de la función exponencial.



RESULTADO:

<img width="226" height="48" alt="image" src="https://github.com/user-attachments/assets/579d1539-0f8f-4d2c-b0e6-d265d92f2e42" />
