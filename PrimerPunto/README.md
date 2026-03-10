# Punto 1 – AFD para movimientos de ajedrez

## Descripción

En este punto se definió una **expresión regular** para reconocer movimientos válidos de ajedrez mediante un **Autómata Finito Determinista (AFD)**.

El objetivo del programa es leer una serie de cadenas desde un archivo y determinar si cada una corresponde a un **movimiento válido de ajedrez** según el formato definido.

---

## Formato de los movimientos

Los movimientos pueden tener la siguiente estructura:

```text
p->k4
qXpe5
```

donde:

* **p, k, q, b, n, r** representan las piezas del ajedrez:

  * p → peón
  * k → rey
  * q → reina
  * b → alfil
  * n → caballo
  * r → torre

* **->** representa un movimiento normal.

* **X** representa una captura de una pieza.

La posición del tablero se expresa mediante:

* una **columna** entre `a` y `h`
* una **fila** entre `1` y `8`

---

## Expresión regular utilizada

```text
(p|k|q|b|n|r)(->|X)(p|k|q|b|n|r)([a-h]?[1-8])
```

Esta expresión permite identificar si una cadena cumple con la estructura de un movimiento válido según las reglas definidas.

---

## Archivo de entrada

El programa lee las cadenas desde el archivo:

```text
pruebas.txt
```

Cada línea contiene un posible movimiento que será evaluado por el AFD.

---

## Ejemplos de entrada

```text
p->k4
qXpe5
r->na3
p-k4
z->k4
kXra8
b->qd2
buentrabajo
123
```

---

## Funcionamiento del programa

El programa procesa cada cadena del archivo y determina si el movimiento es **aceptado o rechazado** según la expresión regular definida.

De esta forma, el AFD permite validar automáticamente si una cadena corresponde a un **movimiento válido de ajedrez** dentro del formato especificado.

