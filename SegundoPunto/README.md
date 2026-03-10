# Punto 2 – AFD para reconocimiento de identificadores
---
## Expresión regular

La expresión regular utilizada es:

```text id="x1n0e4"
[A-Za-z][A-Za-z0-9]*
```

Esta expresión indica que:

* La cadena **debe comenzar con una letra** (`A-Z` o `a-z`).
* Después del primer carácter pueden aparecer **letras o números**.
* No se permiten símbolos especiales.

---

## Diseño del AFD

El autómata está compuesto por **dos estados principales**:

* **q0** → estado inicial
* **q1** → estado de aceptación

### Transiciones

* De **q0 a q1** con cualquier **letra** (`A-Z` o `a-z`).
* De **q1 a q1** con **letras o números** (`A-Z`, `a-z`, `0-9`).

Si aparece **cualquier otro símbolo**, la cadena es **rechazada**.

---

## Ejemplos de prueba

Las siguientes cadenas fueron evaluadas por el programa:

```text id="eh02dd"
numero
1X
hola
x1
parcial
123
como
eufareix10
1variable
_abc
--
1a+2b
a3*b3
a3b3
```

---

## Resultados obtenidos

```text id="1qsjex"
numero ACEPTADO
1X NO ACEPTADO
hola ACEPTADO
x1 ACEPTADO
parcial ACEPTADO
123 NO ACEPTADO
como ACEPTADO
eufareix10 ACEPTADO
1variable NO ACEPTADO
_abc NO ACEPTADO
-- NO ACEPTADO
1a+2b NO ACEPTADO
a3*b3 NO ACEPTADO
a3b3 ACEPTADO
```
