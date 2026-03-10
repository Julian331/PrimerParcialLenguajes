# Implementación en Haskell (Paradigma Funcional)

En Haskell el algoritmo se expresa de manera **más cercana a su definición matemática** mediante funciones recursivas.

Características:

* uso de funciones puras
* ausencia de estado mutable
* estilo declarativo

También se ejecutó el algoritmo **1,000,000 de veces** para medir el tiempo de ejecución.

Resultado aproximado:

```text
9
0.04s
```

---
TIEMPO EN HASKELL:


<img width="654" height="121" alt="image" src="https://github.com/user-attachments/assets/2df01dfb-e2f5-45c8-a3bb-107f1a8b6df7" />


---

# Implementación en C (Paradigma Imperativo)

En C el algoritmo se implementa utilizando **recursión y control explícito del flujo del programa**.

Características:

* manejo directo de variables
* control explícito de la memoria
* ejecución muy cercana al hardware

Para medir el rendimiento, el algoritmo se ejecutó **1,000,000 de veces** utilizando la función `clock()`.

Resultado obtenido:

```text
MCD = 9
Tiempo C: 0.031089 segundos
```

---


TIEMPO EN C:


<img width="684" height="85" alt="image" src="https://github.com/user-attachments/assets/870f287c-6936-43c9-ba87-f843897278c2" />

---


PRUEBAS DE VARIOS NUMEROS EN C:

<img width="785" height="217" alt="image" src="https://github.com/user-attachments/assets/9f56e199-7190-4b5f-95a4-6f7c656be998" />

---

# Comparación de Rendimiento

| Lenguaje | Tiempo aproximado |
| -------- | ----------------- |
| C        | 0.031 s           |
| Haskell  | ~0.04 s           |

Observaciones:

* **C es ligeramente más rápido**, debido a su compilación directa a código máquina.
* **Haskell introduce cierta sobrecarga** debido a su modelo de ejecución funcional y runtime.
* La diferencia es pequeña porque el algoritmo de Euclides es extremadamente eficiente.

---
